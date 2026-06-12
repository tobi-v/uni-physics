from numpy import zeros_like
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

def λ_caseA(length, order, uncertainty=False, Δlength=0):
    '''Stick clamped in the middle'''
    def λ_caseAInner(length, order):
        return 2*length / (2*order - 1 + 1e-10)
    
    return GetResultAndUncertainty(λ_caseAInner, [length, order], uncertainty, [Δlength, zeros_like(Δlength)])

def λ_caseB(length, order, uncertainty=False, Δlength=0):
    '''Stick clamped at 1/4 and 3/4'''
    def λ_caseBInner(length, order):
        return length / (2*order-1 + 1e-10)
    
    return GetResultAndUncertainty(λ_caseBInner, [length, order], uncertainty, [Δlength, zeros_like(Δlength)])