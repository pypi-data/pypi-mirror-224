#!/usr/bin/env python
from setuptools import find_packages
from distutils.core import setup

with open("README.md", "r") as fp:
    long_description = fp.read()

setup(
    name="daisytuner",
    version="0.2.3",
    description="A cloud-connected compiler pass for performance optimization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Lukas Truemper",
    author_email="lukas.truemper@outlook.de",
    url="https://daisytuner.com",
    python_requires=">=3.8",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[
        "requests>=2.11.0",
        "tqdm>=4.64.1",
        "tabulate>=0.9.0",
        "dace>=0.14.3",
        "numpy>=1.23.0",
        "pandas>=1.5.0",
        "scikit-learn>=1.2.0",
        "plotly>=5.11.0",
        "seaborn>=0.2.12",
        "kaleido>=0.2.1",
        "opt_einsum>=3.3.0",
        "torch>=1.13.0",
        "torchvision",
        "torchaudio",
        "torchmetrics>=0.11.4",
        "pytorch-lightning>=1.9.4",
        "torch_geometric>=2.3",
        "jupyterlab>=4.0.3",
    ],
    extras_require={"dev": ["black==22.10.0", "pytest>=7.2.0", "pytest-cov>=4.1.0"]},
    include_package_data=True,
    package_data={
        "daisytuner": ["data/daisynet_v3.ckpt", "data/nvidia_cc_ge_7/*.txt"],
    },
    classifiers=[
        "Topic :: Utilities",
    ],
)
