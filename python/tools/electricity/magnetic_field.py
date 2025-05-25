from numpy import array, cross, pi
from numpy.linalg import norm

mu_0 = 1.257e-6 # [N/A²]

def BiotSavart(I, dv: array, delta_r: array, exclude_singularities=True, singularity_limit = 1e-3) -> array:
    '''return: magnetic field vector
    I: current
    dv: wire segment vector
    delta_r: distance from wire vector'''
    distance = norm(delta_r)
    if(exclude_singularities and (distance < singularity_limit)):
        distance = distance + 1e-3#return array([0, 0, 0])
    return (mu_0*I/(4*pi)) * cross(dv, delta_r) / (distance)**3
