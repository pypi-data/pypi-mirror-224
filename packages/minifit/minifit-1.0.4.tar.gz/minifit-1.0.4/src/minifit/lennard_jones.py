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
Module containing LennardJonesFit class for curve fitting with Lennard-Jones.
"""

import random
from .fit_base import FitBase, log


class LennardJonesFit(FitBase):
    """
    This class makes curve fitting using the Lennard-Jones potential formula.
    It reads data from a file given as the first argument.
    The data file must contain at least two columns.
    The first column represents x values,
    the second and following columns are the y values.
    """

    type_of_fit = "Lennard-Jones potential"
    label_type = "lennard_jones_fit"

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
            ``4 * epsilon * ((sigma / r) ** 12 - (sigma / r) ** 6)``
            it expects ``(val1, val2)`` for sigma, epsilon, such as:
            ``(0.74, 0.34)``
            Otherwise, an exception will be raised. If not passed, a default guess adequate for
            the model function will be used.

        auto_guess:
            (bool) If true, tries to fit until chosen ``precision`` is reached. Default false.

        auto_range:
            (tuple) Sets boundaries for each parameter of the guess.
            If not set, the default range is used. Only used if auto_guess is True.
            Instead of ``guess = (0.74, 0.34)``
            pass ``auto_range = ((0.,10.), (0., 15.))``
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
        r = x
        if len(args) != 2:
            raise TypeError("Passed a wrong number of guess parameters")
        sigma, epsilon = args
        return 4 * epsilon * ((sigma / r) ** 12 - (sigma / r) ** 6)

    def default_guess(self, context):
        """Default guess adequate for the model function."""
        guess = [1, 1]

        return guess

    def random_guess(self, context):
        """
        Random guess adequate for the model function with constraints
        chosen by the user.
        """
        if self.auto_range is None:
            guess = [random.uniform(-60, 60), random.uniform(-60, 60)]
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
        name_temp = ("sigma", "epsilon")
        for el, name_ in enumerate(name_temp):
            log(f"\t {name_}: {popt[el]:2.8f}")

        sigma, epsilon = popt

        log(" ")
        log(" Resulting formula: ")
        log("4 * epsilon * ((sigma / r) ** 12 - (sigma / r) ** 6)")
        log(f"4 * {epsilon} * (({sigma} / r) ** 12 - ({sigma} / r) ** 6)")

    def latex_text(self):
        """Returns a string with the model formula in latex format."""
        sigma, epsilon = self.popt
        n = "\n"
        formula = (
            f"$V = 4 \\varepsilon \\left( \\left( \\frac{{\\sigma}}{{r}} \\right)^{{12}} - "
            f"\\left( \\frac{{\\sigma}}{{r}} \\right)^6 \\right)${n}"
        )
        formula_instance = (
            f"$V = 4 \\cdot {epsilon:.3f} \\left( \\left( \\frac{{{sigma:.3f}}}{{r}} "
            f"\\right)^{{12}} - "
            f"\\left( \\frac{{{sigma:.3f}}}{{r}} \\right)^6 "
            f"\\right)$, {n}where:{n}$\\sigma={sigma}$, $\\varepsilon={epsilon}$"
        )
        return formula + formula_instance
