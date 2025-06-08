from numpy import cos, linspace, ndarray, ones_like, pi, sin, stack

def CreateLoopXYParallel(radius: float, sample_points: ndarray, z: float = 0,)->ndarray:
    '''Returns: Loop around (0,0,z)'''
    phi = linspace(0, 2 * pi, sample_points, endpoint=False)
    x = radius * cos(phi)
    y = radius * sin(phi)
    z_vec = ones_like(x)*z
    return stack((x, y, z_vec), axis=-1)