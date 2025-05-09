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

### Degree of Coupling from in phase and opposite phase periods
def DegreeOfCouplingPhase(t_inPhase, t_oppositePhase, uncertainty=False, delT1=0, delT2=0):
  def DegreeOfCouplingInner(t_inPhase, t_oppositePhase):
    return (t_inPhase**2 - t_oppositePhase**2)/(t_inPhase**2 + t_oppositePhase**2)
  
  return GetResultAndUncertainty(DegreeOfCouplingInner,
                                 [t_inPhase, t_oppositePhase],
                                 uncertainty,
                                 delT1, delT2)