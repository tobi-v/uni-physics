from numpy import allclose, array, array_equal
import pytest
from tools.python.sort import filter_unique_x, sort_by_x_and_filter_unique, sort_by_x

### Tests for filter_unique_x

def test_filter_unique_x_basic():
    x = array([1.0, 2.0, 2.0, 3.0, 1.0])
    y = array([10.0, 20.0, 21.0, 30.0, 11.0])

    x_expected = array([1.0, 2.0, 3.0])
    y_expected = array([10.0, 20.0, 30.0])

    x_unique, y_filtered = filter_unique_x(x, y)

    assert allclose(x_unique, x_expected)
    assert allclose(y_filtered, y_expected)

def test_filter_unique_x_all_unique():
    x = array([1.0, 2.0, 3.0])
    y = array([10.0, 20.0, 30.0])

    x_unique, y_filtered = filter_unique_x(x, y)

    assert allclose(x_unique, x)
    assert allclose(y_filtered, y)

def test_filter_unique_x_all_duplicates():
    x = array([5.0, 5.0, 5.0])
    y = array([10.0, 11.0, 12.0])

    x_expected = array([5.0])
    y_expected = array([10.0])

    x_unique, y_filtered = filter_unique_x(x, y)

    assert allclose(x_unique, x_expected)
    assert allclose(y_filtered, y_expected)

def test_filter_unique_x_empty():
    x = array([])
    y = array([])

    x_unique, y_filtered = filter_unique_x(x, y)

    assert x_unique.size == 0
    assert y_filtered.size == 0

def test_filter_unique_x_length_mismatch():
    x = array([1.0, 2.0])
    y = array([10.0])  # mismatched length

    with pytest.raises(IndexError):
        _ = filter_unique_x(x, y)

### Tests for sort_by_x

def test_sort_by_x_basic():
    x = array([3.0, 1.0, 2.0])
    z = array([30.0, 10.0, 20.0])

    x_expected = array([1.0, 2.0, 3.0])
    z_expected = array([10.0, 20.0, 30.0])

    x_sorted, z_sorted = sort_by_x(x, z)

    assert allclose(x_sorted, x_expected)
    assert allclose(z_sorted, z_expected)

### Tests for


def test_basic_unique_sort():
    x = array([3, 1, 2, 3, 2, 1])
    y = array([30, 10, 20, 300, 200, 100])
    x_unique, y_filtered = sort_by_x_and_filter_unique(x, y)
    assert array_equal(x_unique, array([1, 2, 3]))
    assert array_equal(y_filtered, array([10, 20, 30]))

def test_already_sorted_input():
    x = array([1, 2, 3, 4])
    y = array([10, 20, 30, 40])
    x_unique, y_filtered = sort_by_x_and_filter_unique(x, y)
    assert array_equal(x_unique, x)
    assert array_equal(y_filtered, y)

def test_all_duplicates():
    x = array([5, 5, 5, 5])
    y = array([50, 500, 5000, 50000])
    x_unique, y_filtered = sort_by_x_and_filter_unique(x, y)
    assert array_equal(x_unique, array([5]))
    assert array_equal(y_filtered, array([50]))

def test_empty_arrays():
    x = array([])
    y = array([])
    x_unique, y_filtered = sort_by_x_and_filter_unique(x, y)
    assert x_unique.size == 0
    assert y_filtered.size == 0

def test_non_integer_values():
    x = array([2.5, 3.1, 2.5, 4.0])
    y = array([100, 200, 300, 400])
    x_unique, y_filtered = sort_by_x_and_filter_unique(x, y)
    assert allclose(x_unique, array([2.5, 3.1, 4.0]))
    assert array_equal(y_filtered, array([100, 200, 400]))

def test_negative_values():
    x = array([-1, -2, -1, 0])
    y = array([10, 20, 30, 40])
    x_unique, y_filtered = sort_by_x_and_filter_unique(x, y)
    assert array_equal(x_unique, array([-2, -1, 0]))
    assert array_equal(y_filtered, array([20, 10, 40]))
