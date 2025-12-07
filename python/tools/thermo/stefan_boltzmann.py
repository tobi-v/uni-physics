from numpy.typing import NDArray
from scipy.constants import Stefan_Boltzmann as sigma

def StefanBoltzmann(area: float, T_0: float, delT: NDArray):
    return sigma*area*((T_0 + delT)**4 - T_0**4)