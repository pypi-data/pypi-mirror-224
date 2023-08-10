import dace

from dace.transformation.auto.auto_optimize import make_transients_persistent

from daisytuner.optimization.canonicalization import (
    AutoParallelization,
    GreedyLoopFusion,
    LibraryExpansion,
    LoopSimplification,
)
from daisytuner.optimization.transfer_tuner_pass import TransferTunerPass


class Optimization:
    """ """

    @classmethod
    def apply(
        cls,
        sdfg: dace.SDFG,
        topK: int,
        device: str = "cpu",
        use_profiling_features: bool = False,
    ) -> None:
        # Canonicalization

        LibraryExpansion.apply(sdfg)

        ## First round of auto-parallelization
        AutoParallelization.apply(sdfg)
        LoopSimplification.apply(sdfg)

        ## Second round of auto-parallelization
        AutoParallelization.apply(sdfg)
        LoopSimplification.apply(sdfg)

        ## Greedy loop fusion
        GreedyLoopFusion.apply(sdfg)

        # Tuning
        report = {}
        TransferTunerPass(
            sdfg=sdfg, topK=topK, use_profiling_features=use_profiling_features
        ).apply_pass(sdfg, report)

        # Post-processing
        sdfg.openmp_sections = False
        dace.sdfg.infer_types.infer_connector_types(sdfg)
        dace.sdfg.infer_types.set_default_schedule_and_storage_types(sdfg, None)
        make_transients_persistent(sdfg, dace.DeviceType.CPU)

        return report
