<p align="center"><img src="figures/daisy.png" width="300"/></p>

<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a> 
[![CI](https://github.com/daisytuner/daisytuner/actions/workflows/tests.yml/badge.svg)](https://github.com/daisytuner/daisytuner/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/daisytuner/daisytuner/branch/main/graph/badge.svg?token=44PO0BWG36)](https://codecov.io/gh/daisytuner/daisytuner)

Daisy is a cloud-connected optimization pass for *stateful dataflow multigraphs (SDFG)*. Daisy's optimization is based on the [similarity-based transfer tuning algorithm](https://dl.acm.org/doi/abs/10.1145/3577193.3593714), which fuzzy matches loop transformations from customizable databases using *performance embeddings*.

Installing Daisy is as simple as

```bash
pip install daisytuner
```

### Profiling-Augmented Embeddings

By default, Daisy computes embeddings of loop nests from static features of the SDFG. In order to produce more accurate embeddings, Daisy can additionally use profiling features, which can be automatically computed using the [daisytuner-likwid](https://github.com/daisytuner/daisytuner-likwid) extension. The plugin also enables a variety of further features like automatic roofline modeling. 

### Citation

If you use Daisy, cite us:

```bibtex
@inproceedings{10.1145/3577193.3593714,
    author = {Tr\"{u}mper, Lukas and Ben-Nun, Tal and Schaad, Philipp and Calotoiu, Alexandru and Hoefler, Torsten},
    title = {Performance Embeddings: A Similarity-Based Transfer Tuning Approach to Performance Optimization},
    year = {2023},
    isbn = {9798400700569},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    url = {https://doi.org/10.1145/3577193.3593714},
    doi = {10.1145/3577193.3593714},
    booktitle = {Proceedings of the 37th International Conference on Supercomputing},
    pages = {50–62},
    numpages = {13},
    keywords = {compilers, autotuning, performance optimization, peephole optimization, transfer tuning, embeddings},
    location = {Orlando, FL, USA},
    series = {ICS '23}
}
```
