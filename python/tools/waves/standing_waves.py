from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

def λ_caseA(length, order, uncertainty=False, Δlength=0):
    '''Stick clamped in the middle'''
    def λ_caseAInner(length, order):
        return 2*length / order
    
    return GetResultAndUncertainty(λ_caseAInner, [length, order], uncertainty, [Δlength, 0])