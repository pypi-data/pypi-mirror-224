import dace

from dace.transformation.dataflow import (
    TrivialTaskletElimination,
    AugAssignToWCR,
    MapCollapse,
)
from dace.transformation.interstate import LoopToMap, MoveLoopIntoMap, InlineSDFG
from daisytuner.transformations import GreedyTaskletFusion, TaskletSimplification


class AutoParallelization:
    """ """

    @classmethod
    def apply(cls, sdfg: dace.SDFG) -> None:
        sdfg.apply_transformations_repeated(TrivialTaskletElimination, validate=False)
        sdfg.apply_transformations_repeated(
            (GreedyTaskletFusion, TaskletSimplification), validate=False
        )

        sdfg.apply_transformations_repeated(
            (AugAssignToWCR,), validate=False, permissive=True
        )
        sdfg.apply_transformations_repeated((InlineSDFG, LoopToMap), validate=False)
        dace.propagate_memlets_sdfg(sdfg)
        sdfg.simplify()

        # Move loop into map to facilitate detection of parallel reductions
        sdfg.apply_transformations_repeated((MoveLoopIntoMap,), validate=False)
        sdfg.apply_transformations_repeated(
            (AugAssignToWCR,), validate=False, permissive=True
        )
        sdfg.apply_transformations_repeated((InlineSDFG, LoopToMap), validate=False)
        dace.propagate_memlets_sdfg(sdfg)
        sdfg.simplify()

        sdfg.apply_transformations_repeated(MapCollapse, validate=False)
