from matplotlib.axes import Axes
from numpy import float64, polyfit, poly1d
from numpy.typing import NDArray
from tools.python.checks import CheckLengths
from typing import Tuple

def Linreg(x: NDArray, y: NDArray) -> Tuple[poly1d, NDArray[float64], NDArray[float64]]:
    return Polyreg(x, y, 1)

def Polyreg(
    x: NDArray, y: NDArray, order: int
) -> Tuple[poly1d, NDArray[float64], NDArray[float64]]:
    coeff, cov = polyfit(x, y, deg=order, cov=True)
    return poly1d(coeff), coeff, cov

def PlotWithErrorBars(ax, x, y, linregFunc,
                      x_absErr=0, y_absErr=0, title="", fun_label="", scatter_label="", xlabel="", ylabel="", data_color="k.", error_color="r", fmt="--k", legend_loc='best', grid=True):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.plot(x, linregFunc(x), fmt, label=fun_label)
    ax.errorbar(x, y, fmt=data_color, xerr=x_absErr, yerr=y_absErr, label=scatter_label, ecolor=error_color, capsize=1.5)
    ax.legend(loc=legend_loc)
    ax.grid(visible=grid)


def ScatterWithErrorBars(ax, x, y, x_absErr=0, y_absErr=0,
                         title="", scatter_label="", xlabel="", ylabel="", fmt='k.', legend_loc='best', grid=True):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.errorbar(x, y, fmt=fmt, xerr=x_absErr, yerr=y_absErr, label=scatter_label, ecolor='r', capsize=1.5)
    ax.legend(loc=legend_loc)
    ax.grid(visible=grid)


def PlotLinregWithError(x: NDArray, y: NDArray, ax: Axes, title: str, xlabel="", ylabel=""):
    CheckLengths(x, y)
    linregFunc, coeff, cov = Linreg(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    upper_bound_fun = poly1d([coeff[0] + cov[0][0]**0.5, coeff[1] + cov[1][1]**0.5])
    lower_bound_fun = poly1d([coeff[0] - cov[0][0]**0.5, coeff[1] - cov[1][1]**0.5])
    ax.plot(x, linregFunc(x), '--k', label=f"Linear Regression y={coeff[0]:.2f}x + {coeff[1]:.2f}")
    ax.plot(x, upper_bound_fun(x), ':r', label=f"Upper Bound")
    ax.plot(x, lower_bound_fun(x), ':r', label=f"Lower Bound")
    ax.scatter(x, y, c='b', marker='x', label="Messwerte")
    ax.grid(visible=True)
    ax.legend(loc='best')