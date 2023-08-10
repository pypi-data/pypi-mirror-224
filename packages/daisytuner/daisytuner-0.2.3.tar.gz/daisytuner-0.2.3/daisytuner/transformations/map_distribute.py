import dace
import copy

from dace.sdfg import SDFG
from dace.sdfg import nodes
from dace.sdfg import utils as sdutil
from dace.sdfg.state import SDFGState
from dace.transformation import transformation
from dace.properties import make_properties, Property, EnumProperty


@make_properties
class MapDistribute(transformation.SingleStateTransformation):
    map_entry = transformation.PatternNode(nodes.MapEntry)
    nested_sdfg_node = transformation.PatternNode(nodes.NestedSDFG)
    map_exit = transformation.PatternNode(nodes.MapExit)

    @classmethod
    def expressions(cls):
        return [
            sdutil.node_path_graph(cls.map_entry, cls.nested_sdfg_node, cls.map_exit)
        ]

    def can_be_applied(
        self, state: dace.SDFGState, expr_index: int, sdfg: dace.SDFG, permissive=False
    ):
        nsdfg = self.nested_sdfg_node.sdfg
        nstates = nsdfg.states()
        first_state = nsdfg.start_state

        # Nothing to do
        if len(nstates) <= 1:
            return False

        if len(first_state.nodes()) == 0:
            # Dead state gives spurious errors
            return False

        if len(nsdfg.out_edges(first_state)) > 1:
            return False

        state_transition: dace.InterstateEdge = nsdfg.out_edges(first_state)[0].data
        if not state_transition.is_unconditional() or state_transition.assignments:
            return False

        if state.entry_node(self.map_entry) is not None:
            return False

        return True

    def apply(self, state: SDFGState, sdfg: SDFG):
        nsdfg = self.nested_sdfg_node.sdfg
        nstates = nsdfg.states()
        first_state = nsdfg.start_state

        # Remove first state from original map
        nsdfg.remove_node(first_state)

        # Collect inputs/outputs of first state
        inputs = set()
        outputs = set()
        for access_node in first_state.data_nodes():
            if first_state.in_degree(access_node) == 0:
                inputs.add(access_node.data)
            if first_state.out_degree(access_node) == 0:
                outputs.add(access_node.data)
                for edge in first_state.in_edges(access_node):
                    if edge.data.wcr is not None:
                        inputs.add(access_node.data)
                        break

        # Create new map
        first_map_entry = copy.deepcopy(self.map_entry)
        for conn in list(first_map_entry.in_connectors):
            first_map_entry.remove_in_connector(conn)
        for conn in list(first_map_entry.out_connectors):
            first_map_entry.remove_out_connector(conn)
        state.add_node(first_map_entry)

        first_map_exit = copy.deepcopy(self.map_exit)
        for conn in list(first_map_exit.in_connectors):
            first_map_exit.remove_in_connector(conn)
        for conn in list(first_map_exit.out_connectors):
            first_map_exit.remove_out_connector(conn)

        state.add_node(first_map_exit)

        # Insert first state into new map
        first_nsdfg = dace.SDFG(nsdfg.name + "_0")
        for output in outputs:
            if output not in first_nsdfg.arrays:
                first_nsdfg.add_datadesc(output, copy.deepcopy(nsdfg.arrays[output]))

        for input in inputs:
            if input not in first_nsdfg.arrays:
                first_nsdfg.add_datadesc(input, copy.deepcopy(nsdfg.arrays[input]))

        new_first_state = copy.deepcopy(first_state)
        first_nsdfg.add_node(new_first_state)
        new_first_state.parent = first_nsdfg

        first_nsdfg_node: nodes.NestedSDFG = state.add_nested_sdfg(
            first_nsdfg, parent=sdfg, inputs=inputs, outputs=outputs
        )

        if not inputs:
            state.add_edge(first_map_entry, None, first_nsdfg_node, None, dace.Memlet())

        for oedge in state.out_edges(self.map_entry):
            if oedge.dst_conn not in first_nsdfg_node.in_connectors:
                continue

            if oedge.src_conn not in first_map_entry.out_connectors:
                first_map_entry.add_out_connector(oedge.src_conn)

            state.add_edge(
                first_map_entry,
                oedge.src_conn,
                first_nsdfg_node,
                oedge.dst_conn,
                copy.deepcopy(oedge.data),
            )

        mapped_outputs = set()
        for inedge in state.in_edges(self.map_exit):
            if inedge.src_conn not in first_nsdfg_node.out_connectors:
                continue

            if inedge.dst_conn not in first_map_exit.in_connectors:
                first_map_exit.add_in_connector(inedge.dst_conn)

            state.add_edge(
                first_nsdfg_node,
                inedge.src_conn,
                first_map_exit,
                inedge.dst_conn,
                copy.deepcopy(inedge.data),
            )
            mapped_outputs.add(inedge.data.data)

        # Connect new map
        for inedge in state.in_edges(self.map_entry):
            out_conn = "OUT_" + inedge.dst_conn[3:]
            if out_conn not in first_map_entry.out_connectors:
                continue

            if inedge.dst_conn not in first_map_entry.in_connectors:
                first_map_entry.add_in_connector(inedge.dst_conn)

            state.add_edge(
                inedge.src,
                inedge.src_conn,
                first_map_entry,
                inedge.dst_conn,
                copy.deepcopy(inedge.data),
            )

        intermediate_output_nodes = {}
        for output in mapped_outputs:
            intermediate_output_nodes[output] = state.add_access(output)

        for oedge in state.out_edges(self.map_exit):
            in_conn = "IN_" + oedge.src_conn[4:]
            if in_conn not in first_map_exit.in_connectors:
                continue

            if oedge.dst_conn not in first_map_exit.out_connectors:
                first_map_exit.add_out_connector(oedge.src_conn)

            dst_node = intermediate_output_nodes[oedge.data.data]
            state.add_edge(
                first_map_exit,
                oedge.src_conn,
                dst_node,
                oedge.dst_conn,
                copy.deepcopy(oedge.data),
            )

        for inedge in state.in_edges(self.map_entry):
            if inedge.data.data not in mapped_outputs:
                continue

            inter_node = intermediate_output_nodes[inedge.data.data]
            state.add_edge(
                inter_node,
                inedge.src_conn,
                inedge.dst,
                inedge.dst_conn,
                copy.deepcopy(inedge.data),
            )
            state.remove_edge(inedge)

            if state.out_degree(inedge.src) == 0 and state.in_degree(inedge.src) == 0:
                state.remove_node(inedge.src)

        dace.propagate_memlets_sdfg(sdfg)
