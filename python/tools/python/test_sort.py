from numpy import array, allclose
from tools.python.sort import sort_by_x

def test_sort_by_x_basic():
    x = array([3.0, 1.0, 2.0])
    z = array([30.0, 10.0, 20.0])

    x_expected = array([1.0, 2.0, 3.0])
    z_expected = array([10.0, 20.0, 30.0])

    x_sorted, z_sorted = sort_by_x(x, z)

    assert allclose(x_sorted, x_expected)
    assert allclose(z_sorted, z_expected)
