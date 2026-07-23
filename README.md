# Maros-Meszaros test set for QP solvers

This repository contains the [Maros-Meszaros test set](https://www.cuter.rl.ac.uk/Problems/marmes.html) in a format suitable for [qpbenchmark](https://github.com/qpsolvers/qpbenchmark). Maros-Meszaros is a standard test set containing 138 quadratic programs that are designed to be difficult. Here are the reports produced by `qpbenchmark`:

- 📈 <a href="https://github.com/qpsolvers/maros_meszaros_qpbenchmark/blob/main/results/maros_meszaros.md"><strong>Maros-Meszaros test set results</strong></a>
- 📈 [Dense subset results](https://github.com/qpsolvers/maros_meszaros_qpbenchmark/blob/main/results/maros_meszaros_dense.md)
- 📈 [Sparse subset results](https://github.com/qpsolvers/maros_meszaros_qpbenchmark/blob/main/results/maros_meszaros_sparse.md)

The methodology and limitations of the benchmark are described in the [qpbenchmark readme](https://github.com/qpsolvers/qpbenchmark/).

## Installation

The recommended process is to install the benchmark and all solvers using [pixi](https://pixi.prefix.dev/):

```console
pixi install
```

It is also possible to install the benchmark [from PyPI](https://github.com/qpsolvers/qpbenchmark#installation).

## Usage

Run the test set as follows:

Run the test set as follows:

```console
pixi run maros_meszaros         # full test set
pixi run maros_meszaros_dense   # dense subset
pixi run maros_meszaros_sparse  # sparse subset
```

The outcome is a standardized report comparing all available solvers against the different [benchmark metrics](https://github.com/qpsolvers/qpbenchmark#metrics). You can check out and post your own results in the [Results forum](https://github.com/qpsolvers/maros_meszaros_qpbenchmark/discussions/categories/results).

## Subsets

| Subset name | Description | Problems |
|-------------|-------------|----------|
| - | All problems. | 138 / 138 | [Report](https://github.com/qpsolvers/maros_meszaros_qpbenchmark/blob/main/results/maros_meszaros.md) |
| [Dense](https://github.com/qpsolvers/maros_meszaros_qpbenchmark/blob/main/results/maros_meszaros_dense.md) | Only problems with less than $n \leq 1000$ variables and $m \leq 10000$ constraints. | 62 / 138 |
| [Dense pos. def.](https://github.com/qpsolvers/maros_meszaros_qpbenchmark/blob/main/results/maros_meszaros_dense_posdef.md) | Only problems from the Dense subset where the cost matrix is positive-definite. | 19 / 138 |
| [Sparse](https://github.com/qpsolvers/maros_meszaros_qpbenchmark/blob/main/results/maros_meszaros_sparse.md) | Complementary to the dense subset | 76 / 138 |

## Citation

This test set is run using `qpbenchmark`. If you use it in your work, you can refer to it using [this citation](https://github.com/qpsolvers/qpbenchmark#citation).

## See also

Related test sets that may be relevant to your use cases:

- [Free-for-all](https://github.com/qpsolvers/free_for_all_qpbenchmark): community-built test set, new problems welcome!
- [Model predictive control](https://github.com/qpsolvers/mpc_qpbenchmark): model predictive control problems arising e.g. in robotics.
