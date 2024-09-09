#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

"""Sparse subset of the Maros-Meszaros test set."""

import os
from typing import Iterator

import qpbenchmark
from qpbenchmark.benchmark import main

from maros_meszaros import MarosMeszaros


class MarosMeszarosSparse(MarosMeszaros):
    """Subset of Maros-Meszaros complementary to the dense subset."""

    @property
    def description(self) -> str:
        """Description of the test set."""
        return (
            "Subset of the Maros-Meszaros test set "
            "complementary to the dense subset."
        )

    @property
    def title(self) -> str:
        """Test set title."""
        return "Maros-Meszaros sparse subset"

    @property
    def sparse_only(self) -> bool:
        """Test set is sparse."""
        return True

    def __iter__(self) -> Iterator[qpbenchmark.Problem]:
        """Iterate on test set problems."""
        for problem in super().__iter__():
            nb_variables = problem.P.shape[0]
            nb_constraints = self.count_constraints(problem)
            if nb_variables > 1000 or nb_constraints > 1000:
                yield problem.to_sparse()


if __name__ == "__main__":
    test_set_path = os.path.abspath(__file__)
    test_set_dir = os.path.dirname(test_set_path)
    main(
        test_set_path=test_set_path,
        results_path=f"{test_set_dir}/results/qpbenchmark_results.csv",
    )
