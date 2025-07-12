from numpy import exp, ndarray

def gaussian(x: ndarray, amplitude: float, mean: float, stddev: float) -> ndarray:
    if stddev == 0:
        raise ZeroDivisionError("Standard deviation must be non-zero.")
    return amplitude * exp(-0.5 * ((x - mean) / stddev)**2)
