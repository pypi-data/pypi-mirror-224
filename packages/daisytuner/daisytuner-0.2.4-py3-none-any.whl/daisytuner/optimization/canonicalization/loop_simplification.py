import dace

from dace.transformation.optimizer import Optimizer
from dace.transformation.dataflow import (
    TrivialMapElimination,
    MapCollapse,
    PruneConnectors,
    MapFission,
)
from dace.transformation.interstate import InlineSDFG
from daisytuner.transformations import MapDistribute


class LoopSimplification:
    """ """

    @classmethod
    def apply(cls, sdfg: dace.SDFG) -> None:
        # Pre-conditions
        sdfg.apply_transformations_repeated(TrivialMapElimination, validate=False)

        # Distribute states inside of map into separate maps
        sdfg.apply_transformations_repeated(
            (MapDistribute, PruneConnectors), validate=False
        )
        dace.propagate_memlets_sdfg(sdfg)
        sdfg.simplify()

        while True:
            xforms = Optimizer(sdfg).get_pattern_matches(patterns=(MapFission,))
            target = None
            for xform in xforms:
                state = xform._sdfg.node(xform.state_id)
                map_entry = xform.map_entry
                map_exit = state.exit_node(map_entry)

                if xform.expr_index == 1:
                    if xform._sdfg.parent_nsdfg_node is not None:
                        continue

                    if xform.nested_sdfg.sdfg.has_cycles():
                        continue

                    target = xform
                    break
                else:
                    if state.out_degree(map_exit) == 1:
                        continue

                target = xform

            if target is None:
                break

            state = target._sdfg.node(target.state_id)
            target.apply(state, target._sdfg)

            sdfg.apply_transformations_repeated(
                (MapDistribute, PruneConnectors, InlineSDFG), validate=False
            )
            dace.propagate_memlets_sdfg(sdfg)
            sdfg.simplify()

        sdfg.apply_transformations_repeated(MapCollapse, validate=False)
