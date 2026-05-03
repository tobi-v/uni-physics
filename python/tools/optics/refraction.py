from numpy import arcsin, arctan2, float64, ones_like, pi, sin, sqrt, tan
from numpy.typing import NDArray
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

def snell(α: NDArray[float64], n1:float=1, n2:float=1, uncertainty=False, delα=0, deln1=0, deln2=0):
    def snell_Inner(α: float, n1:float=1, n2:float=1):
        return arcsin((n1/n2)*sin(α))

    return GetResultAndUncertainty(snell_Inner, [α, n1*ones_like(α), n2*ones_like(α)], uncertainty, [delα, deln1, deln2])

def fresnel_rho_p(α: NDArray[float64], n1:float=1, n2:float=1, uncertainty=False, delα=0, deln1=0, deln2=0):
    def rho_p_Inner(α: float, β:float):
        return -tan(α-β)/(tan(α+β) + 1e-6)
    
    if uncertainty:
        β, delβ = snell(α, n1, n2, True, delα, deln1, deln2)
    else:
        β = snell(α, n1, n2)
        delβ = 0
    
    return GetResultAndUncertainty(rho_p_Inner, [α, β], uncertainty, [delα, delβ])

def fresnel_rho_s(α: NDArray[float64], n1:float=1, n2:float=1, uncertainty=False, delα=0, deln1=0, deln2=0):
    def rho_s_Inner(α: float, β:float):
        return -sin(α-β)/(sin(α+β) + 1e-6)
    
    if uncertainty:
        β, delβ = snell(α, n1, n2, True, delα, deln1, deln2)
    else:
        β = snell(α, n1, n2)
        delβ = 0
    
    return GetResultAndUncertainty(rho_s_Inner, [α, β], uncertainty, [delα, delβ])

def airy_trans(fresnel_rho, α: NDArray[float64], d: float, λ: float, n:float=1, δφ=0, uncertainty=False, delα=0, deld=0, delλ=0, deln=0, delδφ=0):
    def airy_trans_Inner(α: NDArray[float64], d: float, λ: float, n:float=1, R=0):
        delta_s = 2*d*sqrt(n**2 - sin(α)**2)
        delta_φ = 2*pi*delta_s/λ + δφ
        delta_φ_mod = delta_φ%(2*pi)
        F = 4*R/(1+1e-6-R)**2

        return 1/(1 + F*sin(delta_φ/2)**2)

    if uncertainty:
        R, delR = fresnel_rho(α, n1=1, n2=n, uncertainty=True, delα=delα, deln1=0, deln2=deln)
        R = R**2
    else:
        R = fresnel_rho(α, n1=1, n2=n)**2
        delR = 0
    
    return GetResultAndUncertainty(airy_trans_Inner, [α, d, λ, n, R], uncertainty, [delα, deld, delλ, deln, delR])

def airy_trans_p(α: NDArray[float64], d: float, λ: float, n:float=1, δφ=0, uncertainty=False, delα=0, deld=0, delλ=0, deln=0, delδφ=0):
    return airy_trans(fresnel_rho_p, α, d, λ, n, δφ, uncertainty, delα, deld, delλ, deln, delδφ)

def airy_trans_s(α: NDArray[float64], d: float, λ: float, n:float=1, δφ=0, uncertainty=False, delα=0, deld=0, delλ=0, deln=0, delδφ=0):
    return airy_trans(fresnel_rho_s, α, d, λ, n, δφ, uncertainty, delα, deld, delλ, deln, delδφ)

def brewster(n1, n2, uncertainty=False, deln1=0, deln2=0):
    def brewster_inner(n1, n2):
        return arctan2(n2, n1)
    
    return GetResultAndUncertainty(brewster_inner, [n1, n2], uncertainty, [deln1, deln2])