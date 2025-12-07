from numpy.typing import NDArray
from scipy.constants import Stefan_Boltzmann as sigma

def StefanBoltzmann(delT: NDArray, area: float, T_0: float):
    return sigma*area*((T_0 + delT)**4 - T_0**4)