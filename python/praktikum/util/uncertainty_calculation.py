import numpy as np
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

def GaussianErrorPropagation(fun, point, uncertainties):
  if(len(point) != len(uncertainties)):
     print(f"Error: point is of length {len(point)}, but uncertainties is of length {len(uncertainties)}")
     return
  
  quadratic_error_sum = 0

  for ii, uncertainty in enumerate(uncertainties):
    part_dev = partial_derivative(fun, ii, point)
    quadratic_error_sum += (part_dev*uncertainty)**2

  return np.sqrt(quadratic_error_sum)

def GetResultAndUncertainty(Fun, point, uncertainty=False, delParam=0):
  if uncertainty:
    propagated_uncertainty = GaussianErrorPropagation(Fun, point, delParam)
    return Fun(*point), propagated_uncertainty
  
  return Fun(*point)

def MeanAndStd(array, axis=0):
   mean = np.mean(array, axis=axis)
   std = np.std(array, axis=axis, ddof=1)
   return mean, std