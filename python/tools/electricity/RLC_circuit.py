from numpy import atan2, pi, sqrt
from numpy.typing import NDArray

def SeriesAmplitude(omega: NDArray, R: float, L: float, C: float) -> NDArray:
    return sqrt(R**2 + (omega*L - 1/(omega*C))**2)


def SeriesPhase(omega: NDArray, R: float, L: float, C: float, deg: bool=False) -> NDArray:
    result = atan2(omega*L - 1/(omega*C), R)
    if deg:
        return result * 180/pi
    else:
        return result