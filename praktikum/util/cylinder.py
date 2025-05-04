import numpy as np
from util.uncertainty_calculation import GaussianErrorPropagation

def MassFromVolume(l, r, rho, uncertainty=False, delL=0, delR=0, delRho=0):
  def MassFromVolumeInner(l, r, rho):
    return rho * np.pi * l * r**2

  if uncertainty:
    propagated_uncertainty = GaussianErrorPropagation(MassFromVolumeInner, [l, r, rho], [delL, delR, delRho])
    return MassFromVolumeInner(l, r, rho), propagated_uncertainty
  return MassFromVolumeInner(l, r, rho)