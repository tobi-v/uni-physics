from numpy import array, cross, pi
from numpy.linalg import norm

mu_0 = 1.257e-6 # [N/A²]

def BiotSavart(current,
               wire_segment: array,
               delta_r: array,
               exclude_singularities=True,
               singularity_limit = 1e-3) -> array:
    '''
    delta_r: distance from wire vector
    
    Returns: magnetic field vector'''
    distance = norm(delta_r)
    if(exclude_singularities and (distance < singularity_limit)):
        distance = distance + 1e-3
    return (mu_0*current/(4*pi)) * cross(wire_segment, delta_r) / (distance)**3
