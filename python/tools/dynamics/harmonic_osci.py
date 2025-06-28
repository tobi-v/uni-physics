from numpy import ndarray, linspace
from scipy.interpolate import UnivariateSpline

def find_resonance_frequency(omega: ndarray, amplitude: ndarray) -> float:
    """
    Estimates the resonance frequency by fitting a spline to the amplitude data
    and locating the frequency at which the interpolated amplitude is maximal.

    Parameters:
        omega (ndarray): 1D array of angular frequencies [rad/s], shape (n,)
        amplitude (ndarray): 1D array of corresponding amplitudes, shape (n,)

    Returns:
        float: Estimated resonance frequency [rad/s]
    """
    # Fit a cubic spline through the data (no smoothing)
    spline = UnivariateSpline(omega, amplitude, s=0)
    
    # Evaluate the spline on a fine frequency grid
    omega_fine = linspace(omega.min(), omega.max(), 10_000)
    amplitude_fine = spline(omega_fine)
    
    # Find the frequency where the spline reaches its maximum
    index_max = amplitude_fine.argmax()
    resonance_frequency = omega_fine[index_max]
    
    return resonance_frequency
