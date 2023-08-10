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
Module containing tests for PolyFit class.
"""

# pylint: skip-file

import pytest
from random import seed
from .common import check_list_within_percentage
from pathlib import Path
from minifit import poly


def test_PolyFit_model_function():
    """Tests for model function"""
    seed(1)
    poly_1 = poly.PolyFit("exp.dat", order=7)
    with pytest.raises(TypeError):
        poly_1.model_function(-1)
    with pytest.raises(TypeError):
        poly_1.model_function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    assert (
        abs(
            poly_1.model_function(-5, 25000, 0.03, 0.003, 5, 4, -3, -2, -1)
            - -1953121981.625
        )
        < 1e-8
    )


def test_PolyFit_results_file():
    "Tests if the pdf with the graph is found in the results directory"
    seed(1)
    poly_1 = poly.PolyFit("example.dat", order=7)
    poly_1()
    file_path = Path.cwd() / "minifit-results" / "polynomial_fit_example_3.pdf"
    assert file_path.exists(), f"File {file_path} does not exist"


def test_PolyFit_popt():
    "Test accuracy of popt found"
    seed(1)
    poly_1 = poly.PolyFit("example.dat", order=7)
    poly_1()
    assert check_list_within_percentage(
        poly_1.popt,
        (
            -2.74662853,
            30.45203439,
            -144.19193953,
            379.07700241,
            -599.65653763,
            572.65814895,
            -305.92156197,
            -39.01693768,
        ),
        1,
    )
    assert not check_list_within_percentage(
        poly_1.popt,
        (
            -2.74662853 * 1.1,
            30.45203439,
            -144.19193953,
            379.07700241,
            -599.65653763,
            572.65814895,
            -305.92156197,
            -39.01693768,
        ),
        1,
    )
    # first element differes by 10%, arrays should not be considered equal if precison is set to 1%


def test_PolyFit_precision():
    """Test precision of the fit"""
    seed(1)
    poly_1 = poly.PolyFit("example.dat", order=7)
    poly_1()
    assert poly_1.sq_root_error <= 6
    poly_1 = poly.PolyFit(
        "poly_order-3.txt", auto_guess=True, precision=0.1, order=3
    )
    poly_1()
    assert poly_1.sq_root_error <= 0.01
