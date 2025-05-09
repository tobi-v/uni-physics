import numpy as np
from scipy.differentiate import derivative

def partial_derivative(func, var=0, point=[]):
    args = point[:]
    def wraps(x):
        args[var] = x
        return func(*args)
    return derivative(wraps, point[var])

def GaussianErrorPropagation(fun, point, uncertainties):
  if(len(point) != len(uncertainties)):
     print(f"Error: point is of length {len(point)}, but uncertainties is of length {len(uncertainties)}")
     return
  
  quadratic_error_sum = 0

  for ii, uncertainty in enumerate(uncertainties):
    part_dev = partial_derivative(fun, ii, point)
    quadratic_error_sum += (part_dev.df*uncertainty)**2

  return np.sqrt(quadratic_error_sum)

def GetResultAndUncertainty(Fun, param, uncertainty=False, delParam=0):
  if uncertainty:
    propagated_uncertainty = GaussianErrorPropagation(Fun, param, delParam)
    return Fun(*param), propagated_uncertainty
  return Fun(*param)

def MeanAndStd(array, axis=0):
   mean = np.mean(array, axis=axis)
   std = np.std(array, axis=axis, ddof=1)
   return mean, std