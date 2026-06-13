from itertools import product
from numpy import abs, empty, max, mean as npmean, ndarray, sqrt, std as npstd
from scipy.differentiate import derivative
from tools.python.checks import CheckLengths


def partial_derivative(func, var=0, point=[]):
    if isinstance(point[var], ndarray):
        derivatives = empty(point[var].size)
        for ii, _ in enumerate(point[var]):
            subpoint = [subl[ii] for subl in point]
            args = subpoint[:]

            def wraps(x):
                args[var] = x
                return func(*args)

            derivatives[ii] = derivative(wraps, subpoint[var]).df
        return derivatives
    else:
        # copy the point, so it doesn't get modified through the loops
        args = point[:]

        def wraps(x):
            args[var] = x
            return func(*args)

        # Adjust initial_step in case your function is limited to a certain interval
        # TODO: Wrap derivative to handle such cases automatically
        return derivative(wraps, point[var], initial_step=0.5).df


def GaussianErrorPropagationMultivariate(fun, point, uncertainties):
    if len(point) != len(uncertainties):
        print(
            f"Error: point is of length {len(point)},"
            f"but uncertainties is of length {len(uncertainties)}"
        )
        return

    quadratic_error_sum = 0

    for ii, uncertainty in enumerate(uncertainties):
        part_dev = partial_derivative(fun, ii, point)
        quadratic_error_sum += (part_dev * uncertainty) ** 2

    return sqrt(quadratic_error_sum)


def GaussianErrorPropagation(fun, point, uncertainty):
    quadratic_error_sum = abs(derivative(fun, point).df * uncertainty)

    return sqrt(quadratic_error_sum)


def GetResultAndUncertainty(fun, point, uncertainty=False, uncertainty_params=0):
    if isinstance(point, (list, ndarray)):
        # TODO: Have this return two bool: First tells if length are the same,
        # second tells if lengths are adjustable
        # (e.g. one array has length 10 and the others are length 10 or scalars,
        # then you can just multiply the scalars by 10)
        CheckLengths(*point) 
    if uncertainty:
        if isinstance(point, list) or isinstance(point, ndarray):
            propagated_uncertainty = GaussianErrorPropagationMultivariate(
                fun, point, uncertainty_params
            )
            return fun(*point), propagated_uncertainty
        else:
            return fun(point), abs(derivative(fun, point).df * uncertainty)

    if isinstance(point, list) or isinstance(point, ndarray):
        return fun(*point)
    else:
        return fun(point)


def MeanAndStd(arr: ndarray, axis=0):
    mean = npmean(arr, axis=axis)
    std = npstd(arr, axis=axis, ddof=1)
    return mean, std

def VertexUncertainty(fun, point, uncertainties, nominal_value: float):
    CheckLengths(point, uncertainties)
    param_variations = []
    for param, uncertainty in zip(point, uncertainties):
        param_variations.append([param + delta*uncertainty for delta in [-1, 0, 1]])

    param_combinations = product(*param_variations)
    deviations = []
    for combination in param_combinations:
        deviations.append(abs(fun(*combination) - nominal_value))

    return max(deviations)
