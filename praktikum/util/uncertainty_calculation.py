import numpy as np
from scipy.misc import derivative

def partial_derivative(func, var=0, point=[]):
    args = point[:]
    def wraps(x):
        args[var] = x
        return func(*args)
    return derivative(wraps, point[var], dx = 1e-6)

def GaussianErrorPropagation(fun, point, uncertainties):
  if(len(point) != len(uncertainties)):
     print(f"Error: point is of length {len(point)}, but uncertainties is of length {len(uncertainties)}")
     return
  
  quadratic_error_sum = 0

  for ii, uncertainty in enumerate(uncertainties):
    part_dev = partial_derivative(fun, ii, point)
    quadratic_error_sum += (part_dev*uncertainty)**2

  return np.sqrt(quadratic_error_sum)

def GetResultAndUncertainty(Fun, param, uncertainty=False, delParam=0):
  if uncertainty:
    propagated_uncertainty = GaussianErrorPropagation(Fun, param, delParam)
    return Fun(*param), propagated_uncertainty
  return Fun(*param)