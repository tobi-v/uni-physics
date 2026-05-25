from numpy import any
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

def f_lensmakers_equation(g, b, uncertainty=False, Δg=0, Δb=0):
    def f_abbildungsverfahren_inner(g, b):
        return 1 / (1 / b + 1 / g)
    
    if any(g==0) or any(b==0):
        raise ValueError("Neither g nor b should be zero")
    
    return GetResultAndUncertainty(f_abbildungsverfahren_inner, [g, b], uncertainty, [Δg, Δb])

def bessel_method(e, a, uncertainty=False, Δe=0, Δa=0):
    def bessel_method_inner(e, a):
        return (a**2 - e**2)/(4*a)
    
    return GetResultAndUncertainty(bessel_method_inner, [e, a], uncertainty, [Δe, Δa])

def serial_focal_length(f1, f2, d=0, uncertainty=False, Δf1=0, Δf2=0, Δd=0):
    def serial_focal_length_inner(f1, f2, d):
        return 1/(1/f1 + 1/f2 - d/(f1*f2))
    
    if any(f1==0) or any(f2==0):
        raise ValueError("Neither g nor b should be zero")
    
    return GetResultAndUncertainty(serial_focal_length_inner, [f1, f2, d], uncertainty, [Δf1, Δf2, Δd])

def d_from_serial_focal_length(f, f1, f2, uncertainty=False, Δf=0, Δf1=0, Δf2=0):
    def d_from_serial_focal_length_inner(f, f1, f2):
        return f1 + f2 - f1*f2/f
    
    if any(f1==0) or any(f2==0) or any(f==0):
        raise ValueError("Neither g nor b should be zero")
    
    return GetResultAndUncertainty(d_from_serial_focal_length_inner, [f, f1, f2], uncertainty, [Δf, Δf1, Δf2])