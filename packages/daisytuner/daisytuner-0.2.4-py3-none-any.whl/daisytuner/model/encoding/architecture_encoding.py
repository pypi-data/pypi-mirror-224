import torch
import numpy as np

from daisytuner.profiling import Benchmarking


class ArchitectureEncoding:
    def __init__(self) -> None:
        self._encoding = None

    def encode(self) -> torch.tensor:
        if self._encoding is not None:
            return self._encoding

        # Gather benchmarking data
        bench = Benchmarking()
        data = bench.analyze()

        vec = np.zeros((11,), dtype=np.float32)
        vec[0] = data["num_sockets"]
        vec[1] = data["cores_per_socket"]
        vec[2] = data["threads_per_core"]
        vec[3] = data["l2_cache"]
        vec[4] = data["l3_cache"]
        vec[5] = data["peakflops"]
        vec[6] = data["peakflops_avx"]
        vec[7] = data["stream_load"]
        vec[8] = data["stream_store"]
        vec[9] = data["stream_copy"]
        vec[10] = data["stream_triad"]

        self._encoding = torch.tensor(vec, dtype=torch.float)[None, :]
        return self._encoding
