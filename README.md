# Maros-Meszaros test set for QP solvers

This repository contains the [Maros-Meszaros test set](https://www.cuter.rl.ac.uk/Problems/marmes.html) in a format suitable for [qpbenchmark](https://github.com/qpsolvers/qpbenchmark). Maros-Meszaros is a standard test set containing 138 quadratic programs that are designed to be difficult. Here is the report produced by `qpbenchmark`:

<p align=center>
  📈 <a href="results/maros_meszaros_ref.md"><strong>Maros-Meszaros test set results</strong></a>
</p>

## Installation

The recommended process is to install the benchmark and all solvers in an isolated environment using ``conda``:

```console
conda env create -f environment.yaml
conda activate qpbenchmark
```

It is also possible to install the benchmark [from PyPI](https://github.com/qpsolvers/qpbenchmark#installation).

## Usage

Run the test set as follows:

```
qpbenchmark ./maros_meszaros.py run
```

The outcome is a standardized report comparing all available solvers against the different [benchmark metrics](https://github.com/qpsolvers/qpbenchmark#metrics). You can check out and post your own results in the [Results forum](https://github.com/qpsolvers/maros_meszaros_qpbenchmark/discussions/categories/results).

## Subsets

Two subsets are distributed in this repository:

| Subset name | Description | Problems | Results |
|-------------|-------------|----------|---------|
| - | All problems. | 138 / 138 | [Report](https://github.com/qpsolvers/maros_meszaros_qpbenchmark/blob/main/results/maros_meszaros_dense_ref.md) |
| Dense | Only problems with less than $n \leq 1000$ variables and $m \leq 10000$ constraints. | 62 / 138 | [Report](https://github.com/qpsolvers/maros_meszaros_qpbenchmark/blob/main/results/maros_meszaros_dense_ref.md) |
| Dense pos. def. | Only problems from the Dense subset where the cost matrix is positive-definite. | 19 / 138 | [Report](https://github.com/qpsolvers/maros_meszaros_qpbenchmark/blob/main/results/maros_meszaros_dense_posdef_ref.md) |

## Citation

If you use `qpbenchmark` in your scientific works, please cite it *e.g.* as follows:

```bibtex
@software{qpbenchmark2023,
  author = {Caron, Stéphane and Zaki, Akram and Otta, Pavel and Arnström, Daniel and Carpentier, Justin},
  license = {Apache-2.0},
  month = nov,
  title = {{qpbenchmark: Benchmark for quadratic programming solvers available in Python}},
  url = {https://github.com/qpsolvers/qpbenchmark},
  version = {1.2.0},
  year = {2023}
}
```

You can also click on ``Cite this repository`` at the top-right of the [repository page](https://github.com/qpsolvers/qpbenchmark/).
