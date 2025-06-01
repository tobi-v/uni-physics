from numpy import pi
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

g = 9.81

def SchwerpunktsLaenge(T,
                    uncertainty=False,
                    delT=0):
  def SchwerpunktsLaengeInner(T):
    return g*T**2 / (4*pi**2)
  
  return GetResultAndUncertainty(SchwerpunktsLaengeInner,
                                 [T],
                                 uncertainty,
                                 [delT])

def IfromPeriod(period, mass, length, uncertainty=False, delT=0, delM=0, delL=0):
  def IfromPeriodInner(period, mass, length):
    return period**2 *mass*g*length / (4*pi**2)
  
  return GetResultAndUncertainty(IfromPeriodInner,
                                 [period, mass, length],
                                 uncertainty,
                                 [delT, delM, delL])

### Functions for coupled pendulum:
# Degree of Coupling from in phase and opposite phase periods
def DegreeOfCouplingPhase(t_inPhase, t_oppositePhase, uncertainty=False, delT=0):
  def DegreeOfCouplingPhaseInner(t_inPhase, t_oppositePhase):
    return (t_inPhase**2 - t_oppositePhase**2)/(t_inPhase**2 + t_oppositePhase**2)
  
  return GetResultAndUncertainty(DegreeOfCouplingPhaseInner,
                                 [t_inPhase, t_oppositePhase],
                                 uncertainty,
                                 [delT, delT])

def DegreeOfCouplingBeat(period, beat_period,
                         uncertainty=False, delTperiod=0, delTbeat=0):
  def DegreeOfCouplingBeatInner(period, beat_period):
    return 2*period*beat_period/(period**2 + beat_period**2)
  
  return GetResultAndUncertainty(DegreeOfCouplingBeatInner,
                                 [period, beat_period],
                                 uncertainty,
                                 [delTperiod, delTbeat])
