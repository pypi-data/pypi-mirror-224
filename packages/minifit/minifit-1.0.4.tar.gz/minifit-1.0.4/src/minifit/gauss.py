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
Module containing GaussFit class for curve fitting with normal distribution.
"""

import random
import numpy as np
from .fit_base import FitBase, log


class GaussFit(FitBase):
    """
    This class makes a curve fitting using the normal distribution
    It reads data from a file given as the first argument.
    The data file must contain at least two columns.
    The first column represents x values,
    the second and following columns are the y values.
    """

    type_of_fit = "Normal distribution"
    label_type = "gauss_fit"

    def __init__(self, filename, **kwargs):
        """
        **Arguments:**

        filename:
            (string) Name of the file that contains data.

        **Keyword arguments:**

        guess:
            (tuple) A guess of the optimal parameters for the model.
            The number of guesses should match
            the arguments that the model function expects.
            The model is defined as:
            ``A * np.exp(-((x - mu) ** 2) / sig**2)``
            it expects ``(val1, val2, val3)`` for A, mu, and sig, such as:
            ``(4.9, 20., 2.85)``
            Otherwise, an exception will be raised. If not passed, a default guess adequate for
            the model function will be used.

        auto_guess:
            (bool) If true, tries to fit until chosen ``precision`` is reached. Default false.

        auto_range:
            (tuple) Sets boundaries for each parameter of the guess.
            If not set, the default range is used. Only used if auto_guess is True.
            Instead of ``guess = (4.9, 20., 2.85)``
            pass ``auto_range = ((0.,10.), (5., 35.), (1., 8.))``
            If fitting takes a lot of time, giving a better range might be helpful.

        precision:
            (float) Used by ``auto_guess``. Default 0.4. Only used if ``auto_guess`` is True.
            If ``auto_guess`` is True and fitting takes a lot of time,
            lowering the ``precision`` may be necessary for convergence.
            Lowering the precision will make the fitting process faster,
            but the quality of the popt may be worse.

        shift:
            (bool) If true, shifts the data. Default false.
                Data can be shifted and it may
                make the convergence of the least squares algorithm easier.
        """

        super().__init__(filename, **kwargs)

    def model_function(self, x, *args, **kwargs):
        """Depends on the module."""
        if len(args) != 3:
            raise TypeError("Passed a wrong number of guess parameters")
        A, mu, sig = args
        return A * np.exp(-((x - mu) ** 2) / sig**2)

    def default_guess(self, context):
        """Default guess adequate for the model function."""
        guess = [2, 2, 3]

        return guess

    def random_guess(self, context):
        """
        Random guess adequate for the model function with constraints
        chosen by the user.
        """
        if self.auto_range is None:
            guess = [
                random.uniform(-60, 60),
                random.uniform(-60, 60),
                random.uniform(-60, 60),
            ]
        else:
            guess = [
                random.uniform(min_val, max_val)
                for min_val, max_val in self.auto_range
            ]

        return guess

    def print_info(self, popt):
        """
        Print info about popt in the format adequate for the model function.
        """
        name_temp = ("A", "mu", "sigma")
        for el, name_ in enumerate(name_temp):
            log(f"\t {name_}: {popt[el]:2.8f}")

        A, mu, sig = popt

        log(" ")
        log(" Resulting formula: ")
        log("A * np.exp(-((x - mu) ** 2) / sig**2)")
        log(f"{A} * np.exp(-((x - {mu}) ** 2) / {sig}**2)")

    def latex_text(self):
        """Returns a string with the formula used by the model in latex format."""
        A, mu, sig = self.popt
        n = "\n"
        formula = (
            f"$y = A \cdot e^{{- \\frac{{(x - \\mu)^2}}{{\\sigma^2}}}}${n}"
        )
        formula_instance = (
            f"$y = {A:.3f} \cdot e^{{- \\frac{{(x - {mu:.3f})^2}}{{{sig:.3f}^2}}}}$, "
            f"{n}where:{n}$A={A}$, $\\mu={mu}$ {n},$\\sigma={sig}$"
        )
        return formula + formula_instance
