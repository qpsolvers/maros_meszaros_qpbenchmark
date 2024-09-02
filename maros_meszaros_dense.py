#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron
# Copyright 2023-2024 Inria

"""Dense subset of the Maros-Meszaros test set."""

import os
from typing import Iterator

import qpbenchmark
from qpbenchmark.benchmark import main

from maros_meszaros import MarosMeszaros


class MarosMeszarosDense(MarosMeszaros):
    """Subset of Maros-Meszaros restricted to smaller dense problems."""

    @property
    def description(self) -> str:
        """Description of the test set."""
        return (
            "Subset of the Maros-Meszaros test set "
            "restricted to smaller dense problems."
        )

    @property
    def title(self) -> str:
        """Test set title."""
        return "Maros-Meszaros dense subset"

    @property
    def sparse_only(self) -> bool:
        """Test set is dense."""
        return False

    @staticmethod
    def count_constraints(problem: qpbenchmark.Problem):
        """Count inequality and equality constraints.

        Notes:
            We only count box inequality constraints once, and only from lower
            bounds. That latter part is specific to this test set.
        """
        m = 0
        if problem.G is not None:
            m += problem.G.shape[0]
        if problem.A is not None:
            m += problem.A.shape[0]
        if problem.lb is not None:
            m += problem.lb.shape[0]
        return m

    def __iter__(self) -> Iterator[qpbenchmark.Problem]:
        """Iterate on test set problems."""
        for problem in super().__iter__():
            nb_variables = problem.P.shape[0]
            nb_constraints = self.count_constraints(problem)
            if nb_variables <= 1000 and nb_constraints <= 1000:
                yield problem.to_dense()


if __name__ == "__main__":
    test_set_path = os.path.abspath(__file__)
    test_set_dir = os.path.dirname(test_set_path)
    main(
        test_set_path=test_set_path,
        results_path=f"{test_set_dir}/results/qpbenchmark_results.csv",
    )
