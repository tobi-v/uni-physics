from numpy import append, cross, ndarray, pi, zeros_like
from numpy.linalg import norm
from scipy.constants import mu_0

def BiotSavart(current: float,
               wire_segment: ndarray,
               delta_r: ndarray,
               exclude_singularities=True,
               singularity_limit = 1e-3) -> ndarray:
    """
    Parameters:
    - delta_r: distance from wire vector
    
    Returns: magnetic field vector"""
    distance = norm(delta_r)
    if(exclude_singularities and (distance < singularity_limit)):
        distance = distance + 1e-3
    return (mu_0*current/(4*pi)) * cross(wire_segment, delta_r) / (distance)**3

def BOfCoilAlongZ(z: ndarray, current: float, radius: float, turns=1) -> ndarray:
    """Magnetic field B_z along the z-axis from a single circular current loop.
    Returns: B_z field (T) at position(s) z
    """
    return turns*mu_0 *current*radius**2 / (2*(z**2 + radius**2)**(3/2))

def BOfLoopNumeric(current: float, loop: ndarray, pos_grid: ndarray) -> ndarray:
    """Calculate magnetic field B on a 3D grid due to a current loop.

    Parameters:
    - loop: (N, 3) array of loop vertices
    - pos_grid: (..., 3) array of observation positions (e.g., meshgrid)

    Returns:
    - B: (..., 3) array of magnetic field vectors at each grid point
    """
    loop = append(loop, [loop[0]], axis=0)
    B = zeros_like(pos_grid)

    for elem, nextElem in zip(loop, loop[1:]):
        dv = nextElem - elem
        r_mid = (elem + nextElem) / 2
        delta_r = r_mid - pos_grid
        B += BiotSavart(current, dv, delta_r)

    return B

def BOfLoopCenter(current, radius):
    """Get the magnetic field vector at the center of a loop"""
    return mu_0*current/(2*radius)

def HelmholtzAlongZ(z: ndarray,
                    current: float,
                    radius: float,
                    distance: float,
                    turns=1) -> ndarray:
    """B_z field along the z-axis
    from two identical coaxial current loops (Helmholtz pair).

    Returns: B_z field (T) at position(s) z
    """
    return BOfCoilAlongZ(z+distance/2, current, radius, turns) \
            + BOfCoilAlongZ(z-distance/2, current, radius, turns)
