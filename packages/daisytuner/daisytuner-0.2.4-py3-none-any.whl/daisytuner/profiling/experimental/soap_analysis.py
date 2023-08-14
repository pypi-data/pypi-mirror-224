import json
import dace
import copy

from typing import Dict

from daisytuner.analysis.parallel_loop_nest import ParallelLoopNest
from daisytuner.profiling.experimental.soap import Solver, perform_soap_analysis


class SOAPAnalysis(Analysis):
    def __init__(
        self,
        loop_nest: ParallelLoopNest,
        address: str = "localhost",
        port: int = 30000,
    ) -> None:
        self._cache_path = loop_nest.cache_folder / "analysis" / "soap_analysis"
        self._loop_nest = loop_nest

        self._address = address
        self._port = port
        self._solver = None

    def __del__(self):
        if self._solver is not None:
            self._solver.disconnect()

    def analyze(self, num_processors: int, cache_size: int) -> Dict:
        report_path = self._cache_path / f"report_{cache_size}.json"
        if report_path.is_file():
            report = json.load(open(report_path, "r"))
            return report

        self._solver = Solver(address=self._address, port=self._port)
        self._solver.connect()

        # "I" is reserved for complex numbers
        sdfg = copy.deepcopy(self._loop_nest.cutout)
        sdfg.replace("I", "__I")

        bytes_per_element = 0
        for _, desc in sdfg.arrays.items():
            b = desc.dtype.bytes
            if b > bytes_per_element:
                bytes_per_element = b
        cache_size_elements = int(cache_size / bytes_per_element)

        result = perform_soap_analysis(
            sdfg=sdfg,
            solver=self._solver,
        )
        Q = result.Q

        # SOAP messes with the symbols in the SDFG, e.g., changes the case
        symbol_map = {"Ss": cache_size_elements, "p": num_processors}
        for sym in Q.free_symbols:
            if str(sym) in sdfg.constants:
                symbol_map[sym] = sdfg.constants[str(sym)]
                continue

            s = str(sym).upper()
            if s in sdfg.constants:
                symbol_map[sym] = sdfg.constants[s]

        report = {
            "Q": str(Q),
            "Q_eval": float(dace.symbolic.evaluate(Q, symbols=symbol_map)),
            "bytes_per_element": bytes_per_element,
            "symbol_map": {str(k): str(v) for k, v in symbol_map.items()},
        }

        self._cache_path.mkdir(exist_ok=True, parents=True)
        with open(report_path, "w") as handle:
            json.dump(report, handle)

        return report
