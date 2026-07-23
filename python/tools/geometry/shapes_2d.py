from numpy import pi
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

def CircleArea(r, uncertainty=False, Δr=0):
    def CircleAreaInner(r):
        return pi*r**2
    
    return GetResultAndUncertainty(CircleAreaInner, [r], uncertainty, [Δr])