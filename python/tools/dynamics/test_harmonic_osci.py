from numpy import array
from tools.dynamics.harmonic_osci import find_resonance_frequency  # Replace 'your_module' with your actual module name

def test_find_resonance_frequency():
    # Simulated data with a peak at ω ≈ 3.0
    omega = array([1.0, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0])
    amplitude = array([0.2, 0.5, 1.2, 2.0, 1.1, 0.6, 0.3])

    resonance = find_resonance_frequency(omega, amplitude)
    
    assert isinstance(resonance, float), "The result should be a float"
    assert 2.8 < resonance < 3.2, f"Resonance frequency {resonance} not in expected range"
