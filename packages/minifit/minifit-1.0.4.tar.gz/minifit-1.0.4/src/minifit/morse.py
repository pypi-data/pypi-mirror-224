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
Module containing MorseFit class for curve fitting with morse.
"""

import random
import numpy as np
from .fit_base import FitBase, log


class MorseFit(FitBase):
    """
    This class makes curve fitting using the
    Generalized Morse Potential Formula.
    It reads data from a file given as the first argument.
    The data file must contain at least two columns.
    The first column represents x values,
    the second and following columns are the y values.
    """

    type_of_fit = "Morse"
    label_type = "morse_fit"

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
            ``de*(1-np.exp(-b0*(x-re)/re*(1+b1*(b0*(x-re)/re)+b2*(b0*(x-re)/re)**2
            +b3*(b0*(x-re)/re)**3+b4*(b0*(x-re)/re)**4+b5*(b0*(x-re)/re)**5
            +b6*(b0*(x-re)/re)**6)))**2-de``
            it expects a tuple, such as:
            ``(re, de, b0, b1, b2, b3, b4, b5, b6)``
            or
            ``(1.1, 109.36948, 2.919051390412818, 2.6012960451552996, 3.9624444493272435,
            -3.836256017508912, 0.07368753155656269, 0.0885673770356121, 0.04092539988145455)``

        auto_guess:
            (bool) If true, tries to fit until chosen ``precision`` is reached. Default false.

        auto_range:
            (tuple) Sets boundaries for each parameter of the guess.
            If not set, the default range is used. Only used if auto_guess is True.
            Instead of ``guess = (re, de, b0, b1, b2, b3, b4, b5, b6)``
            pass
            ``auto_range = (
            (-100, 100),
            (-300, 300),
            (-300, -300),
            (-300, 300),
            (-300, 300),
            (-300, 300),
            (-300, 300),
            (-300, 300)
            )``
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
        if len(args) != 9:
            raise TypeError("Passed a wrong number of guess parameters")
        re, de, b0, b1, b2, b3, b4, b5, b6 = args
        return (
            de
            * (
                1
                - np.exp(
                    -b0
                    * (x - re)
                    / re
                    * (
                        1
                        + b1 * (b0 * (x - re) / re)
                        + b2 * (b0 * (x - re) / re) ** 2
                        + b3 * (b0 * (x - re) / re) ** 3
                        + b4 * (b0 * (x - re) / re) ** 4
                        + b5 * (b0 * (x - re) / re) ** 5
                        + b6 * (b0 * (x - re) / re) ** 6
                    )
                )
            )
            ** 2
            - de
        )

    def default_guess(self, context):
        """Default guess adequate for the model function."""
        guess = [
            context[0],  # re
            context[1],  # de
            10.0,  # b0
            0.1,  # b1
            0.1,  # b2
            0.001,  # b3
            0.001,  # b4
            0.0001,  # b5
            0.000001,  # b6
        ]
        return guess

    def random_guess(self, context):
        """
        Random guess adequate for the model function with constraints
        chosen by the user.
        """
        if self.auto_range is None:
            guess = [
                context[0],  # re
                context[1],  # de
                random.uniform(-50, 50),  # b0
                random.uniform(-10, 10),  # b1
                random.uniform(-10, 10),  # b2
                random.uniform(-10, 10),  # b3
                random.uniform(-0.1, 0.1),  # b4
                random.uniform(-0.1, 0.1),  # b5
                random.uniform(-0.1, 0.1),  # b6
            ]
        else:
            guess = [
                random.uniform(min_val, max_val)
                for min_val, max_val in self.auto_range
            ]

        return guess

    def context_setter(self, xdata, ydata):
        # returns data useful for setting guess in random_gues and default_guess

        re = xdata[np.argmin(ydata)]
        de = np.abs(np.min(ydata))
        return [re, de]

    def print_info(self, popt):
        """
        Print info about popt in the format adequate for the model function.
        """
        name_temp = ("re", "de", "b0", "b1", "b2", "b3", "b4", "b5", "b6")
        for el, name_ in enumerate(name_temp):
            log(f"\t {name_}: {popt[el]:2.8f}")

        re, de, b0, b1, b2, b3, b4, b5, b6 = popt

        log(" ")
        log(" Resulting formula: ")
        log(
            r"""
            de
            * (
                1
                - np.exp(
                    -b0
                    * (x - re)
                    / re
                    * (
                        1
                        + b1 * (b0 * (x - re) / re)
                        + b2 * (b0 * (x - re) / re) ** 2
                        + b3 * (b0 * (x - re) / re) ** 3
                        + b4 * (b0 * (x - re) / re) ** 4
                        + b5 * (b0 * (x - re) / re) ** 5
                        + b6 * (b0 * (x - re) / re) ** 6
                    )
                )
            )
            ** 2
            - de
              """
        )
        log(
            f"""
            {de}
            * (
                1
                - np.exp(
                    -{b0}
                    * (x - {re})
                    / {re}
                    * (
                        1
                        + {b1} * ({b0} * (x - {re}) / {re})
                        + {b2} * ({b0} * (x - {re}) / {re}) ** 2
                        + {b3} * ({b0} * (x - {re}) / {re}) ** 3
                        + {b4} * ({b0} * (x - {re}) / {re}) ** 4
                        + {b5} * ({b0} * (x - {re}) / {re}) ** 5
                        + {b6} * ({b0} * (x - {re}) / {re}) ** 6
                    )
                )
            )
            ** 2
            - {de}
"""
        )

    def latex_text(self):
        re, de, b0, b1, b2, b3, b4, b5, b6 = self.popt
        n = "\n"

        formula = (
            f"$V = D_e \\left( 1 - e^{{-b_0 \\left( \\frac{{x - r_e}}{{r_e}} \\right) \\left( 1 + "
            f"b_1 \\left( b_0 \\frac{{x - r_e}}{{r_e}} \\right) + "
            f"b_2 \\left( b_0 \\frac{{x - r_e}}{{r_e}} \\right)^2 + "
            f"b_3 \\left( b_0 \\frac{{x - r_e}}{{r_e}} \\right)^3 + "
            f"b_4 \\left( b_0 \\frac{{x - r_e}}{{r_e}} \\right)^4 + "
            f"b_5 \\left( b_0 \\frac{{x - r_e}}{{r_e}} \\right)^5 + "
            f"b_6 \\left( b_0 \\frac{{x - r_e}}{{r_e}} \\right)^6 \\right) }} \\right)^2 - D_e$"
        )

        where = (
            f"where:{n}"
            f"$r_e = {re}${n}"
            f"$D_e = {de}${n}"
            f"$b_0 = {b0}${n}"
            f"$b_1 = {b1}${n}"
            f"$b_2 = {b2}${n}"
            f"$b_3 = {b3}${n}"
            f"$b_4 = {b4}${n}"
            f"$b_5 = {b5}${n}"
            f"$b_6 = {b6}$"
        )

        return formula + "\n" + where
