import numpy as np
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

def MassFromVolume(length, radius, rho, uncertainty=False, delL=0, delR=0, delRho=0):
  def MassFromVolumeInner(length, radius, rho):
    return rho * np.pi * length * radius**2
  return GetResultAndUncertainty(MassFromVolumeInner,
                                 [length, radius, rho],
                                 uncertainty, [delL, delR, delRho])
