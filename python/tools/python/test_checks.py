from numpy import array
import pytest
from tools.python.checks import CheckLengths

def test_arrays_same_length():
    """Arrays with same length should pass"""
    CheckLengths(array([1, 2, 3]), array([4, 5, 6]))


def test_arrays_different_lengths():
    """Arrays with different lengths should raise ValueError"""
    with pytest.raises(ValueError):
        CheckLengths(array([1, 2, 3]), array([4, 5]))


def test_multiple_floats():
    """Multiple floats (scalars) should pass"""
    CheckLengths(1.5, 2.7, 3.14)


def test_multiple_ints():
    """Multiple ints (scalars) should pass"""
    CheckLengths(1, 2, 3)


def test_scalar_and_single_element_array():
    """Mix of scalars and single-element arrays should pass"""
    CheckLengths(1.5, array([2]), 3)


def test_scalar_and_multi_element_array():
    """Scalar with multi-element array should raise ValueError"""
    with pytest.raises(ValueError):
        CheckLengths(1.5, array([2, 3]))


def test_single_array_argument():
    """Single array argument should pass"""
    CheckLengths(array([1, 2, 3]))


def test_three_arrays_same_length():
    """Three arrays with same length should pass"""
    CheckLengths(array([1, 2]), array([3, 4]), array([5, 6]))


def test_three_arrays_different_lengths():
    """Three arrays with different lengths should raise ValueError"""
    with pytest.raises(ValueError):
        CheckLengths(array([1, 2]), array([3, 4, 5]), array([6, 7]))


def test_empty_arrays():
    """Empty arrays should pass"""
    CheckLengths(array([]), array([]))


def test_single_scalar():
    """Single scalar argument should pass"""
    CheckLengths(42.0)


def test_multiple_scalars_and_arrays_matching():
    """Scalars and multi-element arrays all with compatible lengths should pass"""
    with pytest.raises(ValueError):
        CheckLengths(2.5, array([1, 2, 3]), array([4, 5, 6]))


def test_floats_and_ints_mixed():
    """Mix of float and int scalars should pass"""
    CheckLengths(1.5, 2, 3.7, 4)
