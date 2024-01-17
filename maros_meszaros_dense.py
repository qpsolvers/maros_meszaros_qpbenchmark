#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron
# Copyright 2023-2024 Inria

"""Dense subset of the Maros-Meszaros test set."""

from typing import Iterator

from maros_meszaros import MarosMeszaros
from qpbenchmark.problem import Problem


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
    def count_constraints(problem: Problem):
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

    def __iter__(self) -> Iterator[Problem]:
        """Iterate on test set problems."""
        for problem in super().__iter__():
            nb_variables = problem.P.shape[0]
            nb_constraints = self.count_constraints(problem)
            if nb_variables <= 1000 and nb_constraints <= 1000:
                yield problem.to_dense()
