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
Module containing logger and FitBase class.
"""

import inspect
import pprint
import warnings
from abc import ABC, abstractmethod
from pathlib import Path
from scipy.optimize import curve_fit
import matplotlib.pyplot as pyplot
import matplotlib
import numpy as np


matplotlib.use("Agg")


__version__ = "1.0.4"


def log(str1):
    """Logger"""
    if str1 == "=":
        print("=" * 100)
    elif str1 == " ":
        print(" ")
    elif str1 == "logoMiniFit":
        logo = r"""
         __  __ _       _ ______ _ _
        |  \/  (_)     (_)  ____(_) |
        | \  / |_ _ __  _| |__   _| |_
        | |\/| | | '_ \| |  __| | | __|
        | |  | | | | | | | |    | | |_
        |_|  |_|_|_| |_|_|_|    |_|\__|

"""
        print(logo)
    else:
        print(f"{str1}")


class FitBase(ABC):
    """
    Base class for all fitting classes
    """

    type_of_fit = "Name of the model"
    label_type = "model_fit"
    x_label = "x_label"
    y_label = "y_label"

    def __init__(self, filename, **kwargs):
        """Common constructor.

        **Arguments:**

        filename:
            (str) name of the file containing the data

        **Keyword arguments:**

        guess:
            (tuple) A guess of the optimal parameters for the model.
            The number of guesses should match
            the arguments that the model function expects.
            For example, for ``PolyFit`` when ``order`` is 2:
            ax^2 + bx + c it expects ``(val1, val2, val3)`` etc.
            It is the case because model function expects three values. For ax+b
            it would expect 2, etc.
            Otherwise, an exception will be raised. If not passed, a default guess adequate for
            the model function will be used.

        auto_guess:
            (bool) If true, tries to fit until chosen ``precision`` is reached. Default false.

        auto_range:
            (tuple) Sets boundaries for each parameter of the guess.
            If not set, the default range is used. Only used if auto_guess is True.
            Instead of ``guess = (5., 10., -3.)``
            pass ``auto_range = ((0.,10.), (5., 15.), (-40., 30.))``
            If fitting takes a lot of time, giving a better range might be helpful.

        precision:
            (float) Used by ``auto_guess``. Default 0.4. Only used if auto_guess is True.
            If auto_guess is True and fitting takes a lot of time, lowering the precision may be
            necessary for convergence. Lowering the precision will make the fitting process faster,
            but the quality of the popt may be worse.
        shift:
            (bool) If true, shifts the data. Default false.
                Data can be shifted and it may
                make the convergence of the least squares algorithm easier.

        type_of_fit:
            (string) Default: ``Name of the model``.
            Will be used for displaying results in the terminal.

        label_type:
            (string) Default: ``model_fit``.
            Will be used for part of the filename of the graph.
        """

        absolute_path = Path(filename)

        # searches for the file in the cwd directory or ./data
        path_data = Path("./data/" + filename)
        path_cwd = Path.cwd() / Path(filename)

        # searches for the file in the directory that contains script
        # and in data folder

        # Get the frame of the calling script
        caller_frame = inspect.currentframe().f_back.f_back

        # Get the path of the filename of the calling script
        caller_filename = caller_frame.f_code.co_filename

        # Get the directory containing the calling script
        caller_dir = Path(caller_filename).resolve().parent

        path_data_parent_dir = caller_dir / "data" / filename
        path_file_parent_dir = caller_dir / filename

        if (
            # cwd
            not path_cwd.exists
            and not path_data.exists()
            and not absolute_path.exists()
            # parent directory
            and not path_file_parent_dir.exists()
            and not path_data_parent_dir.exists()
        ):
            raise FileNotFoundError(
                f"Couldn't find {filename} in the data folder,\n"
                f"current working directory, and by using an absolute path"
            )

        self.filename = filename

        self.guess = kwargs.get("guess", None)

        if kwargs.get("auto_guess") is True:
            self.auto_guess = True
            self.auto_range = kwargs.get("auto_range", None)
        else:
            self.auto_guess = False
            self.auto_range = None

        self.precision = kwargs.get("precision", 0.4)

        self.shift = kwargs.get("shift", False)

        if path_cwd.exists() is True:
            self.read_data(str(path_cwd))
        elif path_data.exists() is True:
            self.read_data(str(path_data))
        elif path_file_parent_dir.exists() is True:
            self.read_data(str(path_file_parent_dir))
        elif path_data_parent_dir.exists() is True:
            self.read_data(str(path_data_parent_dir))
        else:
            self.read_data(str(absolute_path))

        self.popt = None
        self.pcov = None
        self.abs_sum_diff = np.inf
        self.sq_root_error = np.inf

        self.x_label = kwargs.get("x_label", self.x_label)
        self.y_label = kwargs.get("y_label", self.y_label)

    def read_data(self, filename):
        """Reads data from each column then shifts the data if shift is set to True."""
        cols = None
        with open(filename) as file:
            for line in file:
                if not line.startswith("#"):
                    data = [float(x) for x in line.split()]
                    if cols is not None:
                        cols = np.vstack((cols, data))
                    else:
                        cols = np.array(data)
        self.xdata = cols[:, 0]
        self.ydata = cols[:, 1:]

        self.shift_data = self.ydata[-1, :].copy()
        if self.shift is True:
            self.ydata -= self.ydata[-1, :]
        else:
            self.shift_data[self.shift_data != 0] = 0.0

    @abstractmethod
    def model_function(self, x, *args, **kwargs):
        """Depends on the module."""

    @abstractmethod
    def default_guess(self, context):
        """Default guess adequate for the model function."""

    @abstractmethod
    def random_guess(self, context):
        """
        Random guess adequate for the model function with constraints
        chosen by the user.
        """

    @abstractmethod
    def print_info(self, popt):
        """
        Print info about popt in the format adequate for the model function.
        """

    def context_setter(self, xdata, ydata):
        """
        If overwritten can return data useful for setting guess in random_guess and default_guess
        """
        return [xdata, ydata]

    def optimize(self, xdata, ydata, ind):
        """Finds the optimal parameters and corresponding errors."""

        guess = self.default_guess(self.context_setter(xdata, ydata))
        if self.guess is not None:
            guess = self.guess
        if not self.auto_guess:
            self.popt, self.pcov = curve_fit(
                self.model_function, xdata, ydata, p0=guess
            )
        else:
            while True:
                try:
                    self.abs_sum_diff = np.inf
                    self.sq_root_error = np.inf
                    guess = self.random_guess(
                        self.context_setter(xdata, ydata)
                    )

                    self.popt, self.pcov = curve_fit(
                        self.model_function, xdata, ydata, p0=guess
                    )
                    diff = self.model_function(xdata, *self.popt) - ydata
                    self.abs_sum_diff = np.sum(abs(diff))
                    self.sq_root_error = np.sqrt(np.dot(diff, diff))
                except RuntimeError:
                    log(
                        " Unable to fit with the current guess. Trying again with a new one..."
                    )
                finally:
                    if (
                        self.sq_root_error < self.precision
                        and self.abs_sum_diff < self.precision
                    ):
                        break

        log(" Optimization succesful")
        log(" ")

        log(" Guess:")
        pprint.pprint(guess)
        log(" ")

        log(" Optimized fitting parameters:")
        pprint.pprint(list(self.popt))
        self.print_info(self.popt)

        log(" ")

        log(" Differences between fit and data points:")
        diff = self.model_function(xdata, *self.popt) - ydata

        log("    Data\t\tModel\t      Difference")
        for x, y, z in zip(
            ydata, self.model_function(xdata, *self.popt), diff
        ):
            log(
                f"    {x+self.shift_data[ind]:6.8f} {y+self.shift_data[ind]:6.8f}  {z:e}"
            )
        log(" ")

        log(" Covariance matrix:")
        print(f"{self.pcov}")
        self.abs_sum_diff = np.sum(abs(diff))
        log(" ")

        log(f" Absolute sum of differences:  {self.abs_sum_diff:2.3e}")
        self.sq_root_error = np.sqrt(np.dot(diff, diff))
        log(" ")

        log(f" Square root error:            {self.sq_root_error:2.3e}")
        log(" ")

    def latex_text(self):
        """Returns string with formula used by the model in latex format."""
        return "formula in latex format"

    def show(self, xdata, ydata, ind):
        """Saves graph of the results as pdf."""
        trial_x = np.linspace(xdata[0], xdata[-1], 1000)
        model_y = (
            self.model_function(trial_x, *self.popt) + self.shift_data[ind]
        )

        fig = pyplot.figure(figsize=(1.15 * 7.04, 9.6))
        fig.subplots_adjust(hspace=0.5)
        grid = fig.add_gridspec(2, 1, height_ratios=[0.6, 0.4])
        ax1 = fig.add_subplot(grid[0])
        ax2 = fig.add_subplot(grid[1])

        ax1.plot(xdata, ydata + self.shift_data[ind], label="Data", marker="o")
        ax1.plot(trial_x, model_y, "r-", ls="--", label=self.label_type)
        ax1.legend()

        ax1.set_xlabel(self.x_label)
        ax1.set_ylabel(self.y_label)

        ax2.axis("off")
        n = "\n"
        math_text = f"Formula used:{n}"
        math_text += self.latex_text()
        math_text += f"{n}Popt:{n}"
        math_text += str(self.popt)

        ax2.text(
            0.5,
            1,
            math_text,
            fontsize=12,
            ha="center",
            va="top",
            transform=ax2.transAxes,
            multialignment="center",
        )

        base = Path(self.filename)
        name = base.stem
        outname = self.label_type + "_" + name + "_" + str(ind + 1) + ".pdf"
        save_results_to = "./minifit-results/"
        log(f" Saving results to directory: {save_results_to}")
        mf_results = str(Path.cwd()) + "/minifit-results"
        if Path(mf_results).exists() is not True:
            Path(mf_results).mkdir()
        fig.savefig(save_results_to + outname)

    def __call__(self):
        """Calls optimize() and then show() for chosen data."""
        warnings.filterwarnings("ignore")
        matplotlib.use("Agg")

        log("=")
        log(" Simplify curve fitting with ")
        log("logoMiniFit")
        log(f" version {__version__}!")
        log(f" Model used: {self.type_of_fit}")

        log("=")
        log(" ")
        log(f" Reading data from input file: {self.filename}")
        log(" ")
        log(f" Input file contains {self.ydata.shape[1]} different states.")
        log(" ")
        log("=")
        for ind in range(self.ydata.shape[1]):
            log(" ")
            log("=")
            log(f" Fitting curve for state {ind+1}:")
            log("=")
            log(" ")
            try:
                self.optimize(self.xdata, self.ydata[:, ind], ind)
                self.show(self.xdata, self.ydata[:, ind], ind)
            except RuntimeError:
                log(f" Optimization failed for data set {ind+1}")

            log(" Done.")
            log("=")
            log(" ")
            log(" ")
            log(" ")
