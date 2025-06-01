import numpy as np
from numpy import abs, ndarray
from scipy.differentiate import derivative

def partial_derivative(func, var=0, point=[]):    
  if isinstance(point[var], np.ndarray):
    derivatives = np.empty(point[var].size)
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
    return derivative(wraps, point[var]).df

def GaussianErrorPropagationMultivariate(fun, point, uncertainties):
  if(len(point) != len(uncertainties)):
     print(f"Error: point is of length {len(point)},"\
           f"but uncertainties is of length {len(uncertainties)}")
     return
  
  quadratic_error_sum = 0

  for ii, uncertainty in enumerate(uncertainties):
    part_dev = partial_derivative(fun, ii, point)
    quadratic_error_sum += (part_dev*uncertainty)**2

  return np.sqrt(quadratic_error_sum)

def GaussianErrorPropagation(fun, point, uncertainty):
  quadratic_error_sum = abs(derivative(fun, point).df*uncertainty)

  return np.sqrt(quadratic_error_sum)

def GetResultAndUncertainty(fun, point, uncertainty=False, uncertainty_params=0):
  if uncertainty:
    if isinstance(point, list) or isinstance(point, ndarray):
      propagated_uncertainty = GaussianErrorPropagationMultivariate(fun,
                                                                    point,
                                                                    uncertainty_params)
      return fun(*point), propagated_uncertainty
    else:
      return fun(point), abs(derivative(fun, point).df*uncertainty)
  
  if isinstance(point, list) or isinstance(point, ndarray):
    return fun(*point)
  else:
    return fun(point)    

def MeanAndStd(arr: ndarray, axis=0):
   mean = np.mean(arr, axis=axis)
   std = np.std(arr, axis=axis, ddof=1)
   return mean, std