from numpy import argsort, ndarray

def sort_by_x(x: ndarray, y: ndarray) -> tuple[ndarray, ndarray]:
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
