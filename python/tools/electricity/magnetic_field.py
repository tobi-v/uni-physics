from numpy import cross, ndarray, pi
from numpy.linalg import norm
from scipy.constants import mu_0

def BiotSavart(current,
               wire_segment: ndarray,
               delta_r: ndarray,
               exclude_singularities=True,
               singularity_limit = 1e-3) -> ndarray:
    '''
    delta_r: distance from wire vector
    
    Returns: magnetic field vector'''
    distance = norm(delta_r)
    if(exclude_singularities and (distance < singularity_limit)):
        distance = distance + 1e-3
    return (mu_0*current/(4*pi)) * cross(wire_segment, delta_r) / (distance)**3

def BOfLoopAlongZ(z: ndarray, current: float, radius: float) -> ndarray:
    """Magnetic field B_z along the z-axis from a single circular current loop.
    Returns: B_z field (T) at position(s) z
    """
    return mu_0 *current*radius**2 / (2*(z**2 + radius**2)**(3/2))

def HelmholtzAlongZ(z: ndarray, current: float, radius: float, distance: float) -> ndarray:
    """B_z field along the z-axis from two identical coaxial current loops (Helmholtz pair).

    Returns: B_z field (T) at position(s) z
    """
    return BOfLoopAlongZ(z+distance/2, current, radius) \
            + BOfLoopAlongZ(z-distance/2, current, radius)
