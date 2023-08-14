import dace

from dace.transformation import pass_pipeline as ppl
from typing import Any, Dict

from daisytuner.analysis.parallel_loop_nest import ParallelLoopNest
from daisytuner.optimization.transfer_tuner import TransferTuner


@dace.properties.make_properties
class TransferTunerPass(ppl.ScopePass):

    CATEGORY: str = "Optimization"

    def __init__(
        self, sdfg: dace.SDFG, topK: int, use_profiling_features: bool
    ) -> None:
        super().__init__()
        self._sdfg = sdfg
        self._topk = topK
        self._use_profiling_features = use_profiling_features

        self._tuner = TransferTuner()

    def modifies(self) -> ppl.Modifies:
        return ppl.Modifies.Scopes

    def should_reapply(self, modified: ppl.Modifies) -> bool:
        return False

    def apply(
        self,
        scope: dace.nodes.EntryNode,
        state: dace.SDFGState,
        pipeline_results: Dict[str, Any],
    ) -> int:
        if state.entry_node(scope) is not None:
            return

        loop_nest = ParallelLoopNest.create(state.parent, state, scope)
        schedule = self._tuner.tune(
            loop_nest,
            topK=self._topk,
            use_profiling_features=self._use_profiling_features,
        )
        pipeline_results[scope] = schedule
