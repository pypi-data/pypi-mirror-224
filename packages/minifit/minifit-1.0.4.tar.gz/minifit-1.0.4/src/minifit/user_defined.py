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
Module containing UserFit class for curve fitting with model that is passed to UserFit.
"""


import random
from .fit_base import FitBase, log


class UserFit(FitBase):
    """
    This class makes curve fitting using a user defined model.
    It reads data from a file given as the first argument.
    The data file must contain at least two columns.
    The first column represents x values,
    the second and following columns are the y values.
    """

    type_of_fit = "User defined function"
    label_type = "user_fit"

    def __init__(self, filename, **kwargs):
        """
        **Arguments:**

        filename:
            (string) Name of the file that contains data.

        **Keyword arguments:**

        num_param:
            (int) Number of parameters of user defined model function. Mandatory.
            For ax^2 + bx + c ``num_param = 3`` should be passed etc. Used for sanity checks.
            Unique for UserFit.

        model:
            (function/callable) An object that expects ``(x, *args, **kwargs)``
            and returns y value for given arguments. Mandatory. Unique for UserFit.

        type_of_fit:
            (string) Default: ``User defined function``.
            Will be used for displaying results in the terminal.

        label_type:
            (string) Default: `user_fit`.
            Will be used for part of the filename of the graph.

        guess:
            (tuple) A guess of the optimal parameters for the model.
            The number of guesses should match
            the arguments that the model function expects.
            If model is defined as:

            def quadratic_poly(x, `*args`, `**kwargs`):
                a, b, c = args\n
                return `a * x**2 + b * x + c`

            it expects ``(val1, val2, val3)`` for a, b, and c, such as:
            ``(-5., 25., 1.5)``
            Otherwise, an exception will be raised. If not passed, a default guess adequate for
            the model function will be used.

        auto_guess:
            (bool) If true, tries to fit until chosen ``precision`` is reached. Default false.

        auto_range:
            (tuple) Sets boundaries for each parameter of the guess.
            If not set, the default range is used. Only used if auto_guess is True.
            Example usage:

            def quadratic_poly(x, `*args`, `**kwargs`):
                a, b, c = args\n
                `return a * x**2 + b *x + c`

            Instead of ``guess = (5., 10., -3.)``, pass
            ``auto_range = ((0., 10.), (5., 15.), (-40., 30.))``.
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

        self.type_of_fit = kwargs.get("type_of_fit", UserFit.type_of_fit)
        self.label_type = kwargs.get("label_type", UserFit.label_type)

        num_param = kwargs.get("num_param")
        if num_param is None:
            raise ValueError(
                "Missing required parameter: num_param. How many parameters does "
                "your functions have? Required for sanity checks"
            )
        self.num_param = num_param

        user_def_func = kwargs.get("model")
        if user_def_func is not None and callable(user_def_func):
            # The object is a function
            self.user_def_func = user_def_func
        else:
            # The object is not a function or is None
            raise ValueError(
                "Missing required parameter: model. With what function do you want to fit?"
            )

    def model_function(self, x, *args, **kwargs):
        """Depends on the module."""
        if len(args) != self.num_param:
            raise TypeError("Passed a wrong number of guess parameters")
        return self.user_def_func(x, *args, **kwargs)

    def default_guess(self, context):
        """Default guess adequate for the model function."""
        guess = []
        for _ in range(self.num_param):
            guess.append(1.0)
        return guess

    def random_guess(self, context):
        """
        Random guess adequate for the model function with constraints
        chosen by the user.
        """
        if self.auto_range is None:
            guess = []
            for _ in range(self.num_param):
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
        for el in range(self.num_param):
            log(f"\t {el}: {popt[el]:2.8f}")

    def latex_text(self):
        """Returns string with formula used by the model in latex format."""
        return "User-defined model"
