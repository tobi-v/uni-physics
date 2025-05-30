from tools.statistics.uncertainty_calculation import GaussianErrorPropagation

def GravitationalPressure(rho, g, h, uncertainty=False, delRho=0, delG=0, delH=0):
  def GravitationalPressureInner(rho, g, h):
    return rho*g*h
  if uncertainty:
    propagated_uncertainty = GaussianErrorPropagation(GravitationalPressureInner, [rho, g, h], [delRho, delG, delH])
    return GravitationalPressureInner(rho, g, h), propagated_uncertainty
  return GravitationalPressureInner(rho, g, h)
