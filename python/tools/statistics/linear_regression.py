from numpy import float64, polyfit, poly1d
from numpy.typing import NDArray
from typing import Tuple

def linreg(x: NDArray, y: NDArray) -> Tuple[poly1d, NDArray[float64], NDArray[float64]]:
    return polyreg(x, y, 1)

def polyreg(x: NDArray, y: NDArray, order: int) \
    -> Tuple[poly1d, NDArray[float64], NDArray[float64]]:
    coeff, cov = polyfit(x, y, deg=order, cov=True)
    return poly1d(coeff), coeff, cov

def plotWithErrorBars(ax, x, y, linregFunc,
                      x_absErr=0, y_absErr=0, title="", xlabel="", ylabel=""):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.plot(x, linregFunc(x), '--k')
    ax.errorbar(x, y, fmt='k.', xerr=x_absErr, yerr=y_absErr, ecolor='r', capsize=1.5)
