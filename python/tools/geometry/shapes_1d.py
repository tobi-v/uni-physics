from numpy import array, cos, linspace, pi, ones_like, sin, transpose

def CreateLoopXYParallel(radius, z, sample_points)->array:
    '''Returns: Loop around (0,0,z)'''
    phi = linspace(0, 2*pi, sample_points)
    return transpose(array([radius*sin(phi), radius*cos(phi), z*ones_like(phi)]))