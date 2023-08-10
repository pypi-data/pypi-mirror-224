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

"""
Module containing tests for GaussFit class.
"""

# pylint: skip-file

import pytest
from random import seed
from .common import check_list_within_percentage
from pathlib import Path
from minifit import gauss


def test_GaussFit_model_function():
    "Test of the model function"
    seed(1)
    gauss_1 = gauss.GaussFit("exp.dat")
    with pytest.raises(TypeError):
        gauss_1.model_function(-1)
    with pytest.raises(TypeError):
        gauss_1.model_function(1, 2, 3, 4, 5)
    assert (
        abs(gauss_1.model_function(22, 44, 66, 22) - 0.8058881111043039) < 1e-8
    )


def test_GaussFit_results_file():
    "Tests if pdf with the graph is found in results directory"
    seed(1)
    gauss_1 = gauss.GaussFit("gauss_data.txt")
    gauss_1()
    file_path = Path.cwd() / "minifit-results" / "gauss_fit_gauss_data_1.pdf"
    assert file_path.exists(), f"File {file_path} does not exist"


def test_GaussFit_popt():
    "Test accuracy of popt found"
    seed(1)
    gauss_1 = gauss.GaussFit("gauss_data.txt")
    gauss_1()
    assert check_list_within_percentage(
        gauss_1.popt, (4.97587424, 20.00233527, 2.84768795), 1
    )
    assert not check_list_within_percentage(
        gauss_1.popt, (4.97587424 * 1.1, 20.00233527, 2.84768795), 1
    )
    # first element differes by 10%, arrays should not be considered equal if precison is set to 1%


def test_GaussFit_precision():
    """Test precision of the fit"""
    seed(1)
    gauss_1 = gauss.GaussFit("gauss_data.txt")
    gauss_1()
    assert gauss_1.sq_root_error <= 10
    gauss_1 = gauss.GaussFit(
        "gauss_data2.txt", auto_guess=True, precision=0.01
    )
    gauss_1()
    assert gauss_1.sq_root_error <= 0.01
