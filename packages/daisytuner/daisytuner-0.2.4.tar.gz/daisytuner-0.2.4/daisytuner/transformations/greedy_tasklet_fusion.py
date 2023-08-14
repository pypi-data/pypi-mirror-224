import dace

from dace.transformation.dataflow import TaskletFusion


class GreedyTaskletFusion(TaskletFusion):
    def can_be_applied(
        self,
        graph: dace.SDFGState,
        expr_index: int,
        sdfg: dace.SDFG,
        permissive: bool = False,
    ) -> bool:
        if not super().can_be_applied(graph, expr_index, sdfg, permissive):
            return False

        if graph.out_degree(self.t1) > 1:
            return False

        return True
