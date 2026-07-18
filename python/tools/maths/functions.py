from numpy import exp, floating
from numpy.typing import NDArray
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty


def Gaussian(x: NDArray[floating], amplitude: float, mean: float, stddev: float) -> NDArray[floating]:
    if stddev == 0:
        raise ZeroDivisionError("Standard deviation must be non-zero.")
    return amplitude * exp(-0.5 * ((x - mean) / stddev) ** 2)

def Ratio(denominator: NDArray[floating], numerator: NDArray[floating], uncertainty=False, Δdenominator=0, Δnumerator=0) -> NDArray[floating]:
    '''Berechnet das Verhältnis zweier Variablen var2/var1.'''
    def RatioInner(denominator, numerator):
        return numerator/(denominator + 1e-10)
    
    return GetResultAndUncertainty(RatioInner, [denominator, numerator], uncertainty, [Δdenominator, Δnumerator])

def inverse(x, uncertainty=False, Δx=0):
    def inverseInner(x):
        return 1 / (x + 1e-10)
    
    return GetResultAndUncertainty(inverseInner, [x], uncertainty, [Δx])

def Sum(arr, uncertainty=False, Δarr=0):
    def SumInner(*arr):
        return sum(arr)

    return GetResultAndUncertainty(SumInner, [arr], uncertainty, [Δarr])

def Mean(arr, uncertainty=False, Δarr=0):
    def MeanInner(*arr):
        return sum(arr)/len(arr)   # Need to be done like that for correct application of uncertainty calculation

    return GetResultAndUncertainty(MeanInner, [*arr], uncertainty, [*Δarr])
