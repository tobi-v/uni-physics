from numpy import exp, floating
from numpy.typing import NDArray


def Gaussian(x: NDArray[floating], amplitude: float, mean: float, stddev: float) -> NDArray[floating]:
    if stddev == 0:
        raise ZeroDivisionError("Standard deviation must be non-zero.")
    return amplitude * exp(-0.5 * ((x - mean) / stddev) ** 2)

def Ratio(denominator: NDArray[floating], numerator: NDArray[floating]) -> NDArray[floating]:
    '''Berechnet das Verhältnis zweier Variablen var2/var1.'''
    return numerator/denominator