import dace
import sympy
import torch
import warnings
import numpy as np
import torch_geometric as geo

from typing import List, Dict

from dace.sdfg.graph import MultiConnectorEdge
from dace.frontend.operations import detect_reduction_type

from daisytuner.analysis.parallel_loop_nest import ParallelLoopNest
from daisytuner.model.encoding.vocabulary import (
    NodeVocabulary,
    MAX_ARRAY_DIMS,
    MAX_MAP_DIMS,
)
from daisytuner.model.encoding.profiling_encoding import ProfilingEncoding
from daisytuner.model.encoding.architecture_encoding import ArchitectureEncoding


class Encoding:

    VOCABULARY = NodeVocabulary()

    def __init__(self, loop_nest: ParallelLoopNest) -> None:
        self._loop_nest = loop_nest

    def encode(self, use_profiling_features: bool = False):
        # Reset values
        self._element_mapping = {}
        self._x = []
        self._edge_index = [[], []]
        self._edge_attr = []

        # Static Encoding
        self._static_encoding()

        # Convert to numpy ndarrays
        self._x = np.vstack(self._x)
        self._edge_index = np.vstack(
            [
                np.array(self._edge_index[0], dtype=np.int64),
                np.array(self._edge_index[1], dtype=np.int64),
            ]
        )

        if self._edge_attr:
            self._edge_attr = np.vstack(self._edge_attr)
        else:
            self._edge_attr = np.zeros((0, 2))

        # Log2p transformation
        self._x = np.sign(self._x) * np.log2(np.abs(self._x) + 1.0)

        x = torch.tensor(self._x, dtype=torch.float)
        edge_index = torch.tensor(self._edge_index, dtype=torch.long)
        edge_attr = torch.tensor(self._edge_attr, dtype=torch.float)
        data = geo.data.Data(
            x=x,
            edge_index=edge_index,
            edge_attr=edge_attr,
        )
        if use_profiling_features:
            data.arch = ArchitectureEncoding().encode()
            data.counters = ProfilingEncoding.create(self._loop_nest).encode()
        else:
            warnings.warn(
                "Computing embeddings without profiling features. This will produce less accurate embeddings."
            )

        return data, self._element_mapping

    def _static_encoding(self):
        sdfg = self._loop_nest.cutout
        state = sdfg.start_state

        maps = set()
        for node in state.nodes():
            if isinstance(node, dace.nodes.MapEntry):
                maps.add(node)

        for node in state.nodes():
            scope = state.entry_node(node)
            if isinstance(node, dace.nodes.MapExit):
                scope = state.entry_node(scope)

            if scope is not None and scope not in maps:
                continue

            if isinstance(node, dace.nodes.AccessNode):
                self._encode_access_node(sdfg, state, node)
            elif isinstance(node, dace.nodes.MapEntry):
                if node in maps:
                    self._encode_map_entry(sdfg, state, node)
            elif isinstance(node, dace.nodes.MapExit):
                self._encode_map_exit(sdfg, state, node)
            elif isinstance(node, (dace.nodes.Tasklet, dace.nodes.NestedSDFG)):
                continue
            else:
                raise ValueError(f"Node {node} not supported")

        # Encode top-level memlets
        for edge in state.edges():
            src_scope = state.entry_node(edge.src)
            if isinstance(edge.src, dace.nodes.MapExit):
                src_scope = state.entry_node(src_scope)

            dst_scope = state.entry_node(edge.dst)
            if isinstance(edge.dst, dace.nodes.MapExit):
                dst_scope = state.entry_node(dst_scope)

            if not (src_scope is None and dst_scope is None):
                continue

            self._encode_memlet(sdfg, state, edge)
            memlet_id = self._element_mapping[edge]

            src_id = self._element_mapping[edge.src]
            dst_id = self._element_mapping[edge.dst]
            self._add_edge(src_id, memlet_id)
            self._add_edge(memlet_id, dst_id)

        # Encode inner memlets
        for map_entry in maps:
            rng = Encoding.VOCABULARY["MAP_BODY"]
            body_x = np.zeros(Encoding.VOCABULARY.dims, dtype=np.float32)
            body_x[rng[0]] = 1

            self._x.append(body_x)
            body_id = len(self._x) - 1

            map_entry_id = self._element_mapping[map_entry]
            map_exit = state.exit_node(map_entry)
            map_exit_id = self._element_mapping[map_exit]

            for edge in state.out_edges(map_entry):
                self._encode_memlet(sdfg, state, edge)
                memlet_id = self._element_mapping[edge]

                self._add_edge(map_entry_id, memlet_id)
                self._add_edge(memlet_id, body_id)

            for edge in state.in_edges(map_exit):
                self._encode_memlet(sdfg, state, edge)
                memlet_id = self._element_mapping[edge]

                self._add_edge(body_id, memlet_id)
                self._add_edge(memlet_id, map_exit_id)

    def _encode_access_node(
        self, sdfg: dace.SDFG, state: dace.SDFGState, node: dace.nodes.AccessNode
    ) -> None:
        array = sdfg.arrays[node.data]

        rng = Encoding.VOCABULARY["ACCESS_NODE"]
        node_x = np.zeros(Encoding.VOCABULARY.dims, dtype=np.float32)
        node_x[rng[0]] = 1

        # Transient
        node_x[rng[1]] = 1 if array.transient else 0

        # View
        node_x[rng[2]] = 1 if isinstance(array, dace.data.View) else 0

        # Total size
        # Approximation: Divides envenly
        symbol_map = {**sdfg.constants}
        if isinstance(array.total_size, (sympy.Basic, dace.symbolic.SymExpr)):
            for sym in array.total_size.free_symbols:
                if str(sym).startswith("tile"):
                    symbol_map[str(sym)] = 0

            totalsize = dace.symbolic.overapproximate(array.total_size)
            totalsize = int(dace.symbolic.evaluate(totalsize, symbols=symbol_map))
        else:
            totalsize = array.total_size
        node_x[rng[3]] = totalsize

        if isinstance(array, dace.data.Array):
            # Offset
            node_x[rng[4]] = array.start_offset
            # Alignment
            node_x[rng[5]] = array.alignment

        # Data type: bytes
        node_x[rng[6]] = array.dtype.bytes

        rng_offset = 7

        # Data type: one-hot
        ctype = array.dtype.ctype
        i = Encoding.VOCABULARY.dtypes.index(ctype)
        node_x[rng[rng_offset + i]] = 1

        rng_offset = rng_offset + len(Encoding.VOCABULARY.dtypes)

        # Stride
        for i, stride in enumerate(array.strides):
            stride = dace.symbolic.overapproximate(stride)
            stride = int(dace.symbolic.evaluate(stride, symbols=symbol_map))
            node_x[rng[rng_offset + i]] = stride

        # Shape
        rng_offset = rng_offset + MAX_ARRAY_DIMS
        for i, dim in enumerate(array.shape):
            dim = dace.symbolic.overapproximate(dim)
            dim = int(dace.symbolic.evaluate(dim, symbols=symbol_map))
            node_x[rng[rng_offset + i]] = dim

        self._x.append(node_x)
        self._element_mapping[node] = len(self._x) - 1

    def _encode_map_entry(
        self, sdfg: dace.SDFG, state: dace.SDFGState, node: dace.nodes.MapEntry
    ) -> None:
        rng = Encoding.VOCABULARY["MAP_ENTRY"]
        node_x = np.zeros(Encoding.VOCABULARY.dims, dtype=np.float32)

        map_level = 1
        parent = node
        while state.entry_node(parent) is not None:
            parent = state.entry_node(parent)
            map_level += 1

        node_x[rng[0]] = map_level
        node_x[rng[1]] = len(node.map.params)
        node_x[rng[2]] = node.map.collapse

        rng_offset = 3
        assert len(node.map.params) < MAX_MAP_DIMS
        for i, param in enumerate(node.map.params):
            start, stop, step = node.map.range[i]
            if isinstance(start, dace.symbolic.SymExpr):
                start = start.approx
            if isinstance(stop, dace.symbolic.SymExpr):
                stop = stop.approx
            if isinstance(step, dace.symbolic.SymExpr):
                step = step.approx

            map_extend = stop + 1 - start
            variables = set(map(str, map_extend.free_symbols))

            # Dynamic range
            if variables.intersection(node.in_connectors.keys()):
                node_x[rng[rng_offset + i * 2 + 0]] = -1
            else:
                map_extend = float(
                    dace.symbolic.evaluate(map_extend, symbols=sdfg.constants)
                )
                node_x[rng[rng_offset + i * 2 + 0]] = map_extend

            step = float(dace.symbolic.evaluate(step, symbols=sdfg.constants))
            node_x[rng[rng_offset + i * 2 + 1]] = step

        self._x.append(node_x)

        node_id = len(self._x) - 1
        self._element_mapping[node] = node_id

    def _encode_map_exit(
        self, sdfg: dace.SDFG, state: dace.SDFGState, node: dace.nodes.MapExit
    ) -> None:
        rng = Encoding.VOCABULARY["MAP_EXIT"]
        node_x = np.zeros(Encoding.VOCABULARY.dims, dtype=np.float32)
        node_x[rng[0]] = 1

        self._x.append(node_x)
        self._element_mapping[node] = len(self._x) - 1

    def _encode_memlet(
        self,
        sdfg: dace.SDFG,
        state: dace.SDFGState,
        edge: MultiConnectorEdge[dace.Memlet],
    ) -> None:
        memlet = edge.data

        rng = Encoding.VOCABULARY["MEMLET"]
        memlet_x = np.zeros(Encoding.VOCABULARY.dims, dtype=np.float32)

        # Num elements
        num_elements = memlet.num_elements()

        # Approximation: Divides evenly
        symbol_map = {**sdfg.constants}
        if isinstance(num_elements, (sympy.Basic, dace.symbolic.SymExpr)):
            num_elements = dace.symbolic.overapproximate(num_elements)
            for sym in num_elements.free_symbols:
                if str(sym).startswith("tile"):
                    symbol_map[str(sym)] = 0

            try:
                num_elements = int(
                    dace.symbolic.evaluate(num_elements, symbols=symbol_map)
                )
            except:
                num_elements = 0

        num_elements = max(num_elements, 0.0)
        memlet_x[rng[0]] = num_elements

        # Dynamic
        memlet_x[rng[1]] = 1 if memlet.dynamic else 0

        # Indirection
        memlet_x[rng[2]] = 0
        if isinstance(edge.dst, dace.nodes.Tasklet):
            if edge.dst.name == "indirection":
                memlet_x[rng[2]] = 1

        rng_offset = 3

        # WCR
        reduction_index = 0
        if memlet.wcr is not None and str(memlet.wcr) != "":
            redtype = detect_reduction_type(memlet.wcr)
            reduction_index = (
                Encoding.VOCABULARY.reduction_types.index(redtype.name) + 1
            )

        memlet_x[rng[rng_offset + reduction_index]] = 1

        rng_offset = rng_offset + len(Encoding.VOCABULARY.reduction_types) + 1

        # Parameters of all parent maps
        parent_map: dace.nodes.MapEntry = state.entry_node(edge.dst)
        params = []
        while parent_map is not None:
            ps = list(parent_map.map.params)
            ps.reverse()
            params.extend(ps)

            parent_map = state.entry_node(parent_map)

        params.reverse()
        assert len(params) <= MAX_MAP_DIMS

        start_access_matrix = np.zeros(
            (MAX_ARRAY_DIMS, MAX_MAP_DIMS + 1), dtype=np.float32
        )
        stop_access_matrix = np.zeros(
            (MAX_ARRAY_DIMS, MAX_MAP_DIMS + 1), dtype=np.float32
        )
        step_access_vector = np.zeros((MAX_ARRAY_DIMS,), dtype=np.float32)
        # Access matrix: dim of array x map params + offset
        #   [2 * i_0, 0 * i_1, 3 * i_2, offset]
        #   [0 * i_0, i_1, i_2, offset]
        #   [0 * i_0, i_1, i_2, offset]
        if memlet.data is not None:
            for i in range(len(memlet.subset)):
                start, stop, step = memlet.subset[i]

                for access in self._encode_expression(
                    start, params=params, symbol_map=symbol_map
                ):
                    mul, add, var = access

                    # Constant offset
                    start_access_matrix[i, -2] += add

                    if var in params:
                        start_access_matrix[i, params.index(var)] = mul
                    elif var is None:
                        continue
                    else:
                        raise ValueError(f"Unsupported expression {start}")

                for access in self._encode_expression(
                    stop, params=params, symbol_map=symbol_map
                ):
                    mul, add, var = access

                    # Constant offset
                    stop_access_matrix[i, -2] += add

                    if var in params:
                        stop_access_matrix[i, params.index(var)] = mul
                    elif var is None:
                        continue
                    else:
                        raise ValueError(f"Unsupported expression {stop}")

                step_access_vector[i] = int(step)

        start_access_matrix = start_access_matrix.flatten()
        stop_access_matrix = stop_access_matrix.flatten()
        step_access_vector = step_access_vector.flatten()

        access_matrix = np.concatenate(
            [start_access_matrix, stop_access_matrix, step_access_vector]
        )
        memlet_x[rng[rng_offset:]] = access_matrix

        self._x.append(memlet_x)

        node_id = len(self._x) - 1
        self._element_mapping[edge] = node_id

    def _encode_expression(
        self, expr: str, params: List[str], symbol_map: Dict
    ) -> None:
        expr = dace.symbolic.overapproximate(expr)

        if isinstance(expr, (sympy.Max, sympy.Min)):
            if expr.args[0].is_Atom:
                expr = expr.args[1]
            else:
                expr = expr.args[0]

        # Special case: Constant
        try:
            const = int(dace.symbolic.evaluate(expr, symbols=symbol_map))
            return [(0, const, None)]
        except:
            pass

        # Case: 2 * i
        if isinstance(expr, sympy.Mul):
            mult = dace.symbolic.evaluate(expr.args[0], symbols=symbol_map)
            param = str(expr.args[1])
            assert param in params
            return [(mult, 0, param)]

        # Case: i
        if str(expr) in params:
            assert str(expr) in params
            return [(1, 0, str(expr))]

        accesses = {None: [0, 0, None]}
        for arg in expr.args:
            if isinstance(arg, sympy.Mul):
                mult = int(dace.symbolic.evaluate(arg.args[0], symbols=symbol_map))
                param = str(arg.args[1])
                assert param in params
                assert param not in accesses
                accesses[param] = [mult, 0, param]
            elif str(arg) in params:
                accesses[str(arg)] = [1, 0, str(arg)]
            else:
                accesses[None][1] += int(
                    dace.symbolic.evaluate(arg, symbols=symbol_map)
                )

        return accesses.values()

    def _add_edge(self, src_id: int, dst_id: int) -> None:
        self._edge_index[0].append(src_id)
        self._edge_index[1].append(dst_id)

        edge_features = np.zeros((2,), dtype=np.float32)
        edge_features[0] = 1
        self._edge_attr.append(edge_features)

        # Reverse
        self._edge_index[0].append(dst_id)
        self._edge_index[1].append(src_id)

        edge_features = np.zeros((2,), dtype=np.float32)
        edge_features[1] = 1
        self._edge_attr.append(edge_features)
