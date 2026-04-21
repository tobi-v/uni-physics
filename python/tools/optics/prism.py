from numpy import float64, pi, sin
from numpy.typing import NDArray
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

def n_from_δmin(δ_min: NDArray[float64], uncertainty=False, delδ=0) -> NDArray[float64]:
    def n_from_δmin_Inner(δ_min, γ: float = pi/3.):
        return sin((δ_min + γ)/2.) / sin(γ/2.)

    return GetResultAndUncertainty(n_from_δmin_Inner, [δ_min], uncertainty, [delδ])