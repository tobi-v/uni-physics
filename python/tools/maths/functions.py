from numpy import exp, floating
from numpy.typing import NDArray
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty


def Gaussian(x: NDArray[floating], amplitude: float, mean: float, stddev: float) -> NDArray[floating]:
    if stddev == 0:
        raise ZeroDivisionError("Standard deviation must be non-zero.")
    return amplitude * exp(-0.5 * ((x - mean) / stddev) ** 2)

def Ratio(denominator: NDArray[floating], numerator: NDArray[floating]) -> NDArray[floating]:
    '''Berechnet das Verhältnis zweier Variablen var2/var1.'''
    return numerator/denominator

def inverse(x, uncertainty=False, Δx=0):
    def inverseInner(x):
        return 1 / (x + 1e-10)
    
    return GetResultAndUncertainty(inverseInner, [x], uncertainty, [Δx])