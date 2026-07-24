from numpy import atan2, cos, exp, pi, sqrt
from numpy.typing import NDArray
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

def SeriesAmplitude(ω: NDArray, R: float, L: float, C: float) -> NDArray:
    # TODO: Specify which amplitude is calculated here and enable uncertainty calculation
    return sqrt(R**2 + (ω*L - 1/(ω*C))**2)


def SeriesPhase(ω: NDArray, R: float, L: float, C: float, deg: bool=False) -> NDArray:
    # TODO: Specify which phase is calculated here and enable uncertainty calculation
    result = atan2(ω*L - 1/(ω*C), R)
    if deg:
        return result * 180/pi
    else:
        return result
    
def SeriesAmplitudeDecayAtR(t, u_0, R, L, C):
    α = R/(2*L)
    ω_0 = sqrt(1/(L*C))
    ζ = α/ω_0
    ω_d = ω_0 * sqrt(1 - ζ**2)

    return u_0 * exp(-α*t) * cos(ω_d*t)
    
def SeriesAmplitudeAtR(ω: NDArray, R: float, L: float, C: float, uncertainty=False, Δω=0, ΔR=0, ΔL=0, ΔC=0):
    def SeriesAmplitudeAtRInner(ω: NDArray, R: float, L: float, C: float):
        return sqrt(R**2 / (R**2 + (ω*L - 1/(ω*C))**2) )

    return GetResultAndUncertainty(SeriesAmplitudeAtRInner, [ω, R, L, C], uncertainty, [Δω, ΔR, ΔL, ΔC])