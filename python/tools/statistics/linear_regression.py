from numpy import float64, polyfit, poly1d
from numpy.typing import NDArray
from typing import Tuple


def linreg(x: NDArray, y: NDArray) -> Tuple[poly1d, NDArray[float64], NDArray[float64]]:
    return polyreg(x, y, 1)


def polyreg(
    x: NDArray, y: NDArray, order: int
) -> Tuple[poly1d, NDArray[float64], NDArray[float64]]:
    coeff, cov = polyfit(x, y, deg=order, cov=True)
    return poly1d(coeff), coeff, cov

def plotWithErrorBars(ax, x, y, linregFunc,
                      x_absErr=0, y_absErr=0, title="", fun_label="", scatter_label="", xlabel="", ylabel="", data_color="k.", error_color="r", fmt="--k", legend_loc='best', grid=True):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.plot(x, linregFunc(x), fmt, label=fun_label)
    ax.errorbar(x, y, fmt=data_color, xerr=x_absErr, yerr=y_absErr, label=scatter_label, ecolor=error_color, capsize=1.5)
    ax.legend(loc=legend_loc)
    ax.grid(visible=grid)


def scatterWithErrorBars(ax, x, y, x_absErr=0, y_absErr=0,
                         title="", scatter_label="", xlabel="", ylabel="", fmt='k.', legend_loc='best', grid=True):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.errorbar(x, y, fmt=fmt, xerr=x_absErr, yerr=y_absErr, label=scatter_label, ecolor='r', capsize=1.5)
    ax.legend(loc=legend_loc)
    ax.grid(visible=grid)
