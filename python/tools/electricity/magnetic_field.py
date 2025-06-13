from numpy import append, cross, ndarray, pi, where, zeros_like
from numpy.linalg import norm
from scipy.constants import mu_0

def BiotSavart(current: float,
               wire_segment: ndarray,
               delta_r: ndarray,
               eps: float = 1e-10) -> ndarray:
    """
    Parameters:
    - delta_r: (..., 3) displacement vectors from source
    
    Returns: (..., 3) magnetic field vectors"""
    distance = norm(delta_r, axis=-1, keepdims=True)
    distance_safe = where(distance < eps, eps, distance)
    return (mu_0*current/(4*pi)) * cross(wire_segment, delta_r) / distance_safe**3

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
    closed_loop = append(loop, [loop[0]], axis=0)
    B = zeros_like(pos_grid)

    for elem, nextElem in zip(closed_loop, closed_loop[1:]):
        dv = nextElem - elem
        r_mid = (elem + nextElem) *.5
        delta_r = pos_grid - r_mid
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

def BOfPointDipole(M: ndarray, r: ndarray) -> ndarray:
    """
    Compute the magnetic field B_dip from a magnetic dipole M at positions r.

    Parameters:
    - M: ndarray of shape (3,), the magnetic dipole vector
    - r: ndarray of shape (..., 3), observation points

    Returns:
    - B: ndarray of shape (..., 3), magnetic field vectors
    """
    r_squared = sum(r**2, axis=-1, keepdims=True)         # (..., 1)
    M_dot_r = sum(M * r, axis=-1, keepdims=True)          # (..., 1)

    B = (mu_0 / (4 * pi)) * (
        (3 * M_dot_r * r - r_squared * M) / (r_squared**(2.5))
    )  # (..., 3)

    return B
