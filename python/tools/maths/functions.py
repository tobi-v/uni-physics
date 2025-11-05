from numpy import exp
from numpy.typing import NDArray


def Gaussian(x: NDArray, amplitude: float, mean: float, stddev: float) -> NDArray:
    if stddev == 0:
        raise ZeroDivisionError("Standard deviation must be non-zero.")
    return amplitude * exp(-0.5 * ((x - mean) / stddev) ** 2)

def Ratio(var1: NDArray, var2: NDArray) -> NDArray:
    return var2/var1