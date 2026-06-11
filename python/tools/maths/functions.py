from numpy import exp, floating, sqrt
from numpy.typing import NDArray
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

# TODO: Enable multi argument norm with uncertainty calculation
def norm(x, y, uncertainty=False, Δx=0, Δy=0):
    def normInner(x, y):
        return sqrt(x**2 + y**2)
    
    GetResultAndUncertainty(normInner, [x, y], uncertainty, [Δx, Δy])

# TODO: Enable multi argument product with uncertainty calculation
def product(a, b, uncertainty=False, Δa=0, Δb=0):
    def productInner(a, b):
        return a*b
    
    GetResultAndUncertainty(productInner, [a, b], uncertainty, [Δa, Δb])

def gaussian(x: NDArray[floating], amplitude: float, mean: float, stddev: float) -> NDArray[floating]:
    if stddev == 0:
        raise ZeroDivisionError("Standard deviation must be non-zero.")
    return amplitude * exp(-0.5 * ((x - mean) / stddev) ** 2)

def inverse(x, uncertainty=False, Δx=0):
    def inverseInner(x):
        return 1 / (x + 1e-10)
    
    return GetResultAndUncertainty(inverseInner, [x], uncertainty, [Δx])

def ratio(denominator: NDArray[floating], numerator: NDArray[floating], uncertainty=False, Δnumerator=0, Δdenominator=0) -> NDArray[floating]:
    def normInner(numerator, denominator):
        return numerator/denominator
    
    GetResultAndUncertainty(normInner, [numerator, denominator], uncertainty, [Δnumerator, Δdenominator])
