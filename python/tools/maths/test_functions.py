from numpy import allclose, array, linspace, pi, sqrt
from pytest import raises
from tools.maths.functions import Gaussian


def test_peak_at_mean():
    x = array([0.0])
    result = Gaussian(x, amplitude=2.0, mean=0.0, stddev=1.0)
    assert allclose(result, 2.0), "Gaussian should reach its peak at the mean"


def test_symmetry():
    x = array([-1.0, 1.0])
    result = Gaussian(x, amplitude=1.0, mean=0.0, stddev=1.0)
    assert allclose(result[0], result[1]), (
        "Gaussian should be symmetric around the mean"
    )


def test_zero_far_from_mean():
    x = array([1e6])
    result = Gaussian(x, amplitude=1.0, mean=0.0, stddev=1.0)
    assert allclose(result, 0.0, atol=1e-10), "Gaussian should vanish far from the mean"


def test_nonzero_stddev_required():
    x = array([0.0])
    with raises(ZeroDivisionError):
        Gaussian(x, amplitude=1.0, mean=0.0, stddev=0.0)


def test_shape_preservation():
    x = linspace(-5, 5, 100)
    y = Gaussian(x, amplitude=1.0, mean=0.0, stddev=1.0)
    assert x.shape == y.shape, "Output shape should match input shape"


def test_normalized_peak_value():
    x = array([0.0])
    std = 1.0
    amp = 1 / (sqrt(2 * pi) * std)
    result = Gaussian(x, amplitude=amp, mean=0.0, stddev=std)
    expected = amp
    assert allclose(result, expected), (
        "Peak of normalized Gaussian should match amplitude"
    )
