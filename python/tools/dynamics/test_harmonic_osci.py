from numpy import array, exp, linspace, isclose
from tools.dynamics.harmonic_osci import (
    estimate_damping_constant,
    find_resonance_frequency,
)


def test_estimate_damping_constant():
    # Known parameters
    δ_true = 0.75  # true damping constant [1/s]
    A0 = 1.0  # initial amplitude

    # Simulated time and amplitudes
    t = linspace(0, 5, 50)
    amplitudes = A0 * exp(-δ_true * t)

    # Estimate from the function
    δ_estimated = estimate_damping_constant(t, amplitudes)

    # Assert close to true value
    assert isclose(δ_estimated, δ_true, rtol=1e-3), (
        f"Expected δ ≈ {δ_true}, got {δ_estimated}"
    )


def test_find_resonance_frequency():
    # Simulated data with a peak at ω ≈ 3.0
    omega = array([1.0, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0])
    amplitude = array([0.2, 0.5, 1.2, 2.0, 1.1, 0.6, 0.3])

    resonance = find_resonance_frequency(omega, amplitude)

    assert isinstance(resonance, float), "The result should be a float"
    assert 2.8 < resonance < 3.2, (
        f"Resonance frequency {resonance} not in expected range"
    )
