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
Module containing PolyFit class for curve fitting with polynomials.
"""

import random
from .fit_base import FitBase, log


class PolyFit(FitBase):
    """
    This class makes a polynomial curve fitting.
    Order of the polynomial can be chosen.
    It reads data from a file given as the first argument.
    The data file must contain at least two columns.
    The first column represents x values,
    the second and following columns are the y values.
    """

    type_of_fit = "Polynomials"
    label_type = "polynomial_fit"

    def __init__(self, filename, **kwargs):
        """
        **Arguments:**

        filename:
            (string) Name of the file that contains data.

        **Keyword arguments:**

        order:
            (int) Unique for PolyFit. Order of the polynomial. Optional. Default 1.

        guess:
            (tuple) A guess of the optimal parameters for the model.
            The number of guesses should match
            the arguments that the model function expects.
            For ax^2 + bx + c it expects ``(val1, val2, val3)`` such as ``(10, 5, -100)``.
            For ax + b it expects ``(val1, val2)``, such as ``(-1, 1)``, etc.
            Otherwise, an exception will be raised. If not passed, a default guess adequate for
            the model function will be used.

        auto_guess:
            (bool) If true, tries to fit until chosen ``precision`` is reached. Default false.

        auto_range:
            (tuple) Sets boundaries for each parameter of the ``guess``.
            If not set, the default range is used. Only used if ``auto_guess`` is True.
            Instead of ``guess = (5., 10., -3.)``
            pass ``auto_range = ((0.,10.), (5., 15.), (-40., 30.))``
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

        if "order" not in kwargs:
            log("=")
            log("Order of the polynomial wasn't given. Using default (1)")
        self.order = kwargs.get("order", 1)
        super().__init__(filename, **kwargs)

    def model_function(self, x, *args, **kwargs):
        """Depends on the module."""
        if len(args) != self.order + 1:
            raise TypeError("Passed a wrong number of guess parameters")
        val = 0.0
        # ax^order + bx^(order-1) + (...) + cx + d
        for exp in range(self.order + 1):
            val += args[exp] * x ** (self.order - exp)
        return val

    def default_guess(self, context):
        """Default guess adequate for the model function."""
        guess = []
        for _ in range(self.order + 1):
            guess.append(1.0)
        return guess

    def random_guess(self, context):
        """
        Random guess adequate for the model function with constraints
        chosen by the user.
        """
        if self.auto_range is None:
            guess = []
            for _ in range(self.order + 1):
                guess.append(random.uniform(-150, 150))

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
        letters = (
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        )
        for el in range(self.order + 1):
            if el <= 25:
                log(f"\t {letters[el]}: {self.popt[el]:2.8f}")
            else:
                log(f"\t z: {self.popt[el]:2.8f}")

        if self.order == 1:
            polynomial_expression = f"{popt[0]:.8f}x + {popt[1]:.8f}"
            polynomial_general_formula = (
                f"{letters[0]:.8f}x + {letters[1]:.8f}"
            )
        else:
            # Construct the polynomial expression based on the order
            terms = [
                f"{popt[el]:.8f}x^{self.order - el}"
                for el in range(self.order + 1)
            ]
            polynomial_expression = " + ".join(terms)
            terms_letters = [
                f"{letters[el]}x^{self.order - el}"
                for el in range(self.order + 1)
            ]
            polynomial_general_formula = " + ".join(terms_letters)

        log(" ")
        log(" Resulting formula: ")
        log(f"{polynomial_general_formula}")
        log(f"{polynomial_expression}")

    def latex_text(self):
        letters = (
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        )

        if self.order == 1:
            polynomial_expression = f"{self.popt[0]:.2f}x + {self.popt[1]:.2f}"
            polynomial_general_formula = (
                f"{letters[0]:.2f}x + {letters[1]:.2f}"
            )
        else:
            # Construct the polynomial expression based on the order
            terms = [
                f"${self.popt[el]:.2f}x^{self.order - el}$"
                for el in range(self.order + 1)
            ]
            polynomial_expression = " + ".join(terms)
            terms_letters = [
                f"${letters[el]}x^{self.order - el}$"
                for el in range(self.order + 1)
            ]
            polynomial_general_formula = " + ".join(terms_letters)

            polynomial_general_formula = polynomial_general_formula.replace(
                "x^5$", "x^5$\n"
            ).replace("x^10$", "x^10$\n")
            polynomial_general_formula = polynomial_general_formula.replace(
                "x^15$", "x^15$\n"
            ).replace("x^20$", "x^20$\n")
            polynomial_expression = polynomial_expression.replace(
                "x^5$", "x^5$\n"
            ).replace("x^10$", "x^10$\n")
            polynomial_expression = polynomial_expression.replace(
                "x^15$", "x^15$\n"
            ).replace("x^20$", "x^20$\n")
        where = "where:\n"
        for el in range(self.order + 1):
            if el <= 25:
                where += f"{letters[el]}: {self.popt[el]:2.8f}, "
            else:
                where += f"z: {self.popt[el]:2.8f}, "
            if el % 5 == 0:
                where += "\n"
        result = (
            "$y = $"
            + polynomial_general_formula
            + "\n"
            + "$y = $"
            + polynomial_expression
            + "\n"
            + where
        )

        return result
