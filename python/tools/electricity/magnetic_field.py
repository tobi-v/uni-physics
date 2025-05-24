from numpy import array, cross, linalg, pi

mu_0 = 1.257e-6 # [N/A²]

def BiotSavart(I, dv: array, delta_r: array) -> array:
    '''return: magnetic field vector
    I: current
    dv: wire segment vector
    delta_r: distance from wire vector'''
    return (mu_0*I/(4*pi)) * cross(dv, delta_r) / linalg.norm(delta_r)**3
