from __future__ import annotations

import dace
import networkx as nx

from pathlib import Path

from dace.sdfg.state import StateSubgraphView
from dace.sdfg.analysis.cutout import SDFGCutout


class ParallelLoopNest(object):
    """
    A loop nest, in which all loops are parallel loops (maps).
    """

    __create_key = object()

    def __init__(
        self,
        create_key: object,
        sdfg: dace.SDFG,
        state: dace.SDFGState,
        view: StateSubgraphView,
        cutout: dace.SDFG,
    ) -> None:
        assert create_key == ParallelLoopNest.__create_key

        self._sdfg = sdfg
        self._state = state
        self._view = view
        self._cutout = cutout
        self._cache_folder = Path(cutout.build_folder) / "daisy"
        self._cache_folder.mkdir(exist_ok=True, parents=False)

        self._tree = nx.DiGraph()
        for node in view.nodes():
            if isinstance(node, dace.nodes.MapEntry):
                self._tree.add_node(node)

        for node in self._tree.nodes():
            parent = self._state.entry_node(node)
            if parent is None:
                continue

            self._tree.add_edge(parent, node)

        assert self._tree.number_of_nodes() > 0
        assert nx.is_tree(self._tree)

    @property
    def sdfg(self) -> dace.SDFG:
        return self._sdfg

    @property
    def state(self) -> dace.SDFGState:
        return self._state

    @property
    def view(self) -> StateSubgraphView:
        return self._view

    @property
    def cutout(self) -> dace.SDFG:
        return self._cutout

    @property
    def name(self) -> str:
        return self._cutout.name

    @property
    def hash(self) -> str:
        return self._cutout.hash_sdfg()

    @property
    def cache_folder(self) -> Path:
        return self._cache_folder

    @property
    def tree(self) -> nx.Graph:
        return self._tree

    def levels(self) -> int:
        return nx.dag_longest_path_length(self._tree) + 1

    @classmethod
    def create(
        cls,
        sdfg: dace.SDFG,
        state: dace.SDFGState,
        map_entry: dace.nodes.MapEntry,
        build_folder: str = None,
    ) -> ParallelLoopNest:
        assert map_entry is not None and isinstance(map_entry, dace.nodes.MapEntry)
        assert state.entry_node(map_entry) is None

        map_exit = state.exit_node(map_entry)
        subgraph_nodes = set(state.all_nodes_between(map_entry, map_exit))
        subgraph_nodes.add(map_entry)
        subgraph_nodes.add(map_exit)

        for edge in state.in_edges(map_entry):
            subgraph_nodes.add(edge.src)
        for edge in state.out_edges(map_exit):
            subgraph_nodes.add(edge.dst)

        subgraph_nodes = list(subgraph_nodes)

        # Define subgraph
        view: StateSubgraphView = StateSubgraphView(state, subgraph_nodes)

        # Create independent cutout
        cutout: dace.SDFG = SDFGCutout.singlestate_cutout(
            state,
            *subgraph_nodes,
            make_copy=False,
            make_side_effects_global=False,
            use_alibi_nodes=False,
        )
        cutout.name = "maps_" + str(cutout.hash_sdfg()).replace("-", "_")
        cutout.validate()

        for sym, val in sdfg.constants.items():
            if sym in cutout.free_symbols:
                cutout.specialize({sym: val})

        # Create build folder
        if build_folder is None:
            build_folder = Path(sdfg.build_folder) / "daisy" / "maps" / cutout.name

        Path(build_folder).mkdir(exist_ok=True, parents=True)
        cutout.build_folder = str(build_folder)

        return ParallelLoopNest(
            create_key=cls.__create_key,
            sdfg=sdfg,
            state=state,
            view=view,
            cutout=cutout,
        )
