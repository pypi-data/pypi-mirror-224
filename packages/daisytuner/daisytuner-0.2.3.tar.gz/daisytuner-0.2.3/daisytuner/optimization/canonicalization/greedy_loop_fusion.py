import dace

from dace.transformation import pass_pipeline as ppl
from dace.transformation.dataflow import MapCollapse, MapFusion, MapExpansion


class GreedyLoopFusion:
    """ """

    @classmethod
    def apply(cls, sdfg: dace.SDFG) -> int:
        sdfg.apply_transformations_repeated(MapFusion, validate=False)
