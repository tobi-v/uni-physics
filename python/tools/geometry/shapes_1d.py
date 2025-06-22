from numpy import cos, linspace, ndarray, ones_like, pi, sin, stack

def CreateLoopXYParallel(radius: float, sample_points: ndarray, z: float = 0,) -> ndarray:
    '''Returns: Loop around (0,0,z)'''
    phi = linspace(0, 2 * pi, sample_points, endpoint=False)
    x = radius * cos(phi)
    y = radius * sin(phi)
    z_vec = ones_like(x)*z
    return stack((x, y, z_vec), axis=-1)

def CreateCoilXYParallel(radius: float, sample_points: int, z0: float, length: float, turns: int) -> ndarray:
    """
    Creates a coil made of circular loops in the xy-plane, centered around z0.

    Args:
        sample_points: Number of discrete points per loop.
        z0: z-position of the coil center.
        length: Total axial length of the coil along z-axis.
        turns: Number of turns (loops) in the coil.

    Returns:
        ndarray of shape (turns * sample_points, 3): All points on the coil.
    """
    if turns < 1:
        raise ValueError("Number of turns must be >= 1")
    if sample_points < 3:
        raise ValueError("At least 3 sample points per loop are recommended.")

    z_start = z0 - length / 2
    z_end   = z0 + length / 2
    z_positions = linspace(z_start, z_end, turns)

    coil_points = [CreateLoopXYParallel(radius, sample_points, z) for z in z_positions]
    return stack(coil_points, axis=0).reshape(-1, 3)
