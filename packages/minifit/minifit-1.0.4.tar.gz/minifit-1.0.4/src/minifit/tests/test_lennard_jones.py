# -*- coding: utf-8 -*-
# Copyright (C) 2023-- Michał Kopczyński
#
# This file is part of MiniFit.
#
# MiniFit is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# MiniFit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
#

import pytest
from random import seed
from .common import check_list_within_percentage
from pathlib import Path
from minifit import lennard_jones

"""
Module containing tests for LennardJonesFit class.
"""

# pylint: skip-file


def test_LennardJonesFit_model_function():
    seed(1)
    "Tests of the model function"
    l_j_1 = lennard_jones.LennardJonesFit("exp.dat")
    with pytest.raises(TypeError):
        l_j_1.model_function(-1)
    with pytest.raises(TypeError):
        l_j_1.model_function(1, 2, 3, 4)
    assert abs(l_j_1.model_function(0.01, 0.02, 0.039) - 628.992) < 1e-8


def test_LennardJonesFit_results_file():
    seed(1)
    "Tests if the pdf with the graph is found in the results directory"
    l_j_1 = lennard_jones.LennardJonesFit(
        "foo_data.txt", auto_guess=True, precision=5, shift=True
    )
    l_j_1()
    file_path = (
        Path.cwd() / "minifit-results" / "lennard_jones_fit_foo_data_2.pdf"
    )
    assert file_path.exists(), f"File {file_path} does not exist"


def test_LennardJonesFit_popt():
    "Test accuracy of popt found"
    seed(1)
    l_j_1 = lennard_jones.LennardJonesFit(
        "foo_data.txt", auto_guess=False, guess=(0.75, 0.26), shift=True
    )
    l_j_1()
    assert check_list_within_percentage(
        l_j_1.popt, (0.75353688, 0.26085384), 10
    )
    assert not check_list_within_percentage(
        l_j_1.popt, (0.75353688 * 1.1, 0.26085384), 1
    )
    # first element differes by 10%, arrays should not be considered equal if precison is set to 1%


def test_LennardJonesFit_precision():
    seed(1)
    """Test precision of the fit"""
    l_j_1 = lennard_jones.LennardJonesFit(
        "foo_data.txt", auto_guess=True, precision=5, shift=True
    )
    l_j_1()
    assert l_j_1.sq_root_error <= 5
    l_j_1 = lennard_jones.LennardJonesFit(
        "lennard-jones_data.txt", auto_guess=True, precision=0.01
    )
    l_j_1()
    assert l_j_1.sq_root_error <= 0.01
