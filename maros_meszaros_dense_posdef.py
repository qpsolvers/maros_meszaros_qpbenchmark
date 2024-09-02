#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron
# Copyright 2023-2024 Inria

"""Dense subset with positive definite P of the Maros-Meszaros test set."""

import os
from typing import Iterator

from maros_meszaros_dense import MarosMeszarosDense

import qpbenchmark
from qpbenchmark.benchmark import main
from qpbenchmark.utils import is_posdef


class MarosMeszarosDensePosdef(MarosMeszarosDense):
    """Subset of Maros-Meszaros restricted to smaller dense problems."""

    @property
    def description(self) -> str:
        """Description of the test set."""
        return (
            "Subset of the Maros-Meszaros test set "
            "restricted to smaller dense problems "
            "with positive definite Hessian matrix."
        )

    @property
    def title(self) -> str:
        """Test set title."""
        return "Maros-Meszaros dense positive definite subset"

    @property
    def sparse_only(self) -> bool:
        """Test set is dense."""
        return False

    def __iter__(self) -> Iterator[qpbenchmark.Problem]:
        """Iterate on test set problems."""
        for problem in super().__iter__():
            if is_posdef(problem.P):
                yield problem


if __name__ == "__main__":
    test_set_path = os.path.abspath(__file__)
    test_set_dir = os.path.dirname(test_set_path)
    main(
        test_set_path=test_set_path,
        results_path=f"{test_set_dir}/results/qpbenchmark_results.csv",
    )
