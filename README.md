# Maros-Meszaros test set for QP solvers

This repository contains the [Maros-Meszaros test set](https://www.cuter.rl.ac.uk/Problems/marmes.html) in a format suitable for [qpbenchmark](https://github.com/qpsolvers/qpbenchmark). Maros-Meszaros is a standard test set containing 138 quadratic programs that are designed to be difficult. Here is the report produced by `qpbenchmark`:

- 📈 <a href="https://github.com/qpsolvers/maros_meszaros_qpbenchmark/blob/main/results/maros_meszaros.md"><strong>Maros-Meszaros test set results</strong></a>
- 📈 [Dense subset results](https://github.com/qpsolvers/maros_meszaros_qpbenchmark/blob/main/results/maros_meszaros_dense.md)

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
| - | All problems. | 138 / 138 | [Report](https://github.com/qpsolvers/maros_meszaros_qpbenchmark/blob/main/results/maros_meszaros.md) |
| Dense | Only problems with less than $n \leq 1000$ variables and $m \leq 10000$ constraints. | 62 / 138 | [Report](https://github.com/qpsolvers/maros_meszaros_qpbenchmark/blob/main/results/maros_meszaros_dense.md) |
| Dense pos. def. | Only problems from the Dense subset where the cost matrix is positive-definite. | 19 / 138 | [Report](https://github.com/qpsolvers/maros_meszaros_qpbenchmark/blob/main/results/maros_meszaros_dense_posdef.md) |

## Citation

If you use `qpbenchmark` in your works, please cite all its contributors as follows:

```bibtex
@software{qpbenchmark2024,
  title = {{qpbenchmark: Benchmark for quadratic programming solvers available in Python}},
  author = {Caron, Stéphane and Zaki, Akram and Otta, Pavel and Arnström, Daniel and Carpentier, Justin and Yang, Fengyu and Leziart, Pierre-Alexandre},
  url = {https://github.com/qpsolvers/qpbenchmark},
  license = {Apache-2.0},
  version = {2.3.0},
  year = {2024}
}
```

## See also

Related test sets that may be relevant to your use cases:

- [Free-for-all](https://github.com/qpsolvers/free_for_all_qpbenchmark): community-built test set, new problems welcome!
- [Model predictive control](https://github.com/qpsolvers/mpc_qpbenchmark): model predictive control problems arising e.g. in robotics.
