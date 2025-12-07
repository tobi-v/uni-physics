from numpy.typing import NDArray
from scipy.constants import Stefan_Boltzmann as sigma

def StefanBoltzmann(delT: NDArray, area: float, T_0: float):
    return sigma*area*((T_0 + delT)**4 - T_0**4)

def StefanBoltzmannRelativeResistance(delR: NDArray, area: float, temp_coeff: float, T_0: float):
    return sigma*area*((T_0 + temp_coeff*delR)**4 - T_0**4)