from numpy import argsort, unique
from numpy.typing import NDArray
from typing import Tuple

def filter_unique_x(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    """
    Removes duplicate values in `x` and the corresponding values in `y`.

    Keeps only the first occurrence of each unique value in `x`.

    Parameters:
    ----------
    x : ndarray
        Input array possibly containing duplicates.
    y : ndarray
        Corresponding array to be filtered identically.

    Returns:
    -------
    x_unique : ndarray
        Array of unique values from `x`.
    y_filtered : ndarray
        Values from `y` corresponding to the unique values in `x`.
    """
    _, unique_indices = unique(x, return_index=True)
    x_unique = x[unique_indices]
    y_filtered = y[unique_indices]
    return x_unique, y_filtered

def sort_by_x(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    """
    Sorts the array `x` in increasing order and reorders `y` 
    to match the sorted order of `x`.

    Parameters:
    ----------
    x : ndarray
        The array to sort by
    y : ndarray
        The array to reorder according to the sorted order of `x`

    Returns:
    -------
    x_sorted : ndarray
        The sorted version of `x`.
    y_sorted : ndarray
        The reordered version of `y` corresponding to `x_sorted`.
    """
    sorted_indices = argsort(x)
    x_sorted = x[sorted_indices]
    y_sorted = y[sorted_indices]
    return x_sorted, y_sorted

def sort_by_x_and_filter_unique(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    """
    Removes duplicate values from `x`, keeping only the first occurrence,
    and sorts the resulting unique values in increasing order. Applies the
    same filtering and sorting to `y` based on `x`.

    Parameters:
    ----------
    x : ndarray
        Input array that may contain duplicates and may be unsorted.
    y : ndarray
        Array with values corresponding to `x`.

    Returns:
    -------
    x_unique_sorted : ndarray
        Sorted array of unique values from `x`.
    y_sorted_filtered : ndarray
        Values from `y` corresponding to the sorted unique values in `x`.
    """
    x_unique_sorted, unique_indices = unique(x, return_index=True)

    y_filtered_sorted = y[unique_indices]
    return x_unique_sorted, y_filtered_sorted

