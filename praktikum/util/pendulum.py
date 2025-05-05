from numpy import pi
from util.uncertainty_calculation import GetResultAndUncertainty

def SchwerpunktsLaenge(T,
                    uncertainty=False,
                    delT=0):
  def SchwerpunktsLaengeInner(T):
    g = 9.81
    return g*T**2 / (4*pi**2)
  
  return GetResultAndUncertainty(SchwerpunktsLaengeInner,
                                 [T],
                                 uncertainty,
                                 [delT])