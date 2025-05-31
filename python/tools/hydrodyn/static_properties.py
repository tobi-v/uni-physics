from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

def GravitationalPressure(rho, g, h, uncertainty=False, delRho=0, delG=0, delH=0):
  def GravitationalPressureInner(rho, g, h):
    return rho*g*h
  return GetResultAndUncertainty(GravitationalPressureInner, [rho, g, h], uncertainty, [delRho, delG, delH])

def RhoFromGravitationalPresure(p, g, h, uncertainty=False, delP=0, delG=0, delH=0):
  def RhoFromGravitationalPresureInner(p, g, h):
    return p/(g*h)
  return GetResultAndUncertainty(RhoFromGravitationalPresureInner, [p, g, h], uncertainty, [delP, delG, delH])
