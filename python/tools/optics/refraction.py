from numpy import arcsin, arctan2, float64, ones_like, pi, sin, sqrt, tan
from numpy.typing import NDArray
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

def snell(α: NDArray[float64], n1:float=1, n2:float=1, uncertainty=False, Δα=0, Δn1=0, Δn2=0):
    def snell_Inner(α: float, n1:float=1, n2:float=1):
        return arcsin((n1/n2)*sin(α))

    return GetResultAndUncertainty(snell_Inner, [α, n1*ones_like(α), n2*ones_like(α)], uncertainty, [Δα, Δn1, Δn2])

def fresnel_ρ_p(α: NDArray[float64], n1:float=1, n2:float=1, uncertainty=False, Δα=0, Δn1=0, Δn2=0):
    def rho_p_Inner(α: float, β:float):
        return -tan(α-β)/(tan(α+β) + 1e-6)
    
    if uncertainty:
        β, Δβ = snell(α, n1, n2, True, Δα, Δn1, Δn2)
    else:
        β = snell(α, n1, n2)
        Δβ = 0
    
    return GetResultAndUncertainty(rho_p_Inner, [α, β], uncertainty, [Δα, Δβ])

def fresnel_ρ_s(α: NDArray[float64], n1:float=1, n2:float=1, uncertainty=False, Δα=0, Δn1=0, Δn2=0):
    def rho_s_Inner(α: float, β:float):
        return -sin(α-β)/(sin(α+β) + 1e-6)
    
    if uncertainty:
        β, Δβ = snell(α, n1, n2, True, Δα, Δn1, Δn2)
    else:
        β = snell(α, n1, n2)
        Δβ = 0
    
    return GetResultAndUncertainty(rho_s_Inner, [α, β], uncertainty, [Δα, Δβ])

def airy_trans(fresnel_rho, α: NDArray[float64], d: float, λ: float, n:float=1, δφ=0, uncertainty=False, Δα=0, Δd=0, Δλ=0, Δn=0, Δδφ=0):
    def airy_trans_Inner(α: NDArray[float64], d: float, λ: float, n:float=1, R=0):
        delta_s = 2*d*sqrt(n**2 - sin(α)**2)
        delta_φ = 2*pi*delta_s/λ + δφ
        delta_φ_mod = delta_φ%(2*pi)
        F = 4*R/(1+1e-6-R)**2

        return 1/(1 + F*sin(delta_φ/2)**2)

    if uncertainty:
        R, ΔR = fresnel_rho(α, n1=1, n2=n, uncertainty=True, Δα=Δα, Δn1=0, Δn2=Δn)
        R = R**2
    else:
        R = fresnel_rho(α, n1=1, n2=n)**2
        ΔR = 0
    
    return GetResultAndUncertainty(airy_trans_Inner, [α, d, λ, n, R], uncertainty, [Δα, Δd, Δλ, Δn, ΔR])

def airy_trans_p(α: NDArray[float64], d: float, λ: float, n:float=1, δφ=0, uncertainty=False, Δα=0, Δd=0, Δλ=0, Δn=0, Δδφ=0):
    return airy_trans(fresnel_ρ_p, α, d, λ, n, δφ, uncertainty, Δα, Δd, Δλ, Δn, Δδφ)

def airy_trans_s(α: NDArray[float64], d: float, λ: float, n:float=1, δφ=0, uncertainty=False, Δα=0, Δd=0, Δλ=0, Δn=0, Δδφ=0):
    return airy_trans(fresnel_ρ_s, α, d, λ, n, δφ, uncertainty, Δα, Δd, Δλ, Δn, Δδφ)

def brewster(n1, n2, uncertainty=False, Δn1=0, Δn2=0):
    def brewster_inner(n1, n2):
        return arctan2(n2, n1)
    
    return GetResultAndUncertainty(brewster_inner, [n1, n2], uncertainty, [Δn1, Δn2])

def simple_refl(fresnel_ρ, α: NDArray[float64], n1:float=1, n2:float=1, uncertainty=False, Δα=0, Δn1=0, Δn2=0):
    def simple_refl_inner(ρ: NDArray[float64]):
        return ρ**2

    ρ, Δρ = fresnel_ρ(α, n1=n1, n2=n2, uncertainty=True, Δα=Δα, Δn1=Δn1, Δn2=Δn2)

    return GetResultAndUncertainty(simple_refl_inner, [ρ], uncertainty, [Δρ])

def simple_refl_p(α: NDArray[float64], n1:float=1, n2:float=1, uncertainty=False, Δα=0, Δn1=0, Δn2=0):
    return simple_refl(fresnel_ρ_p, α, n1, n2, uncertainty, Δα, Δn1, Δn2)

def simple_refl_s(α: NDArray[float64], n1:float=1, n2:float=1, uncertainty=False, Δα=0, Δn1=0, Δn2=0):
    return simple_refl(fresnel_ρ_s, α, n1, n2, uncertainty, Δα, Δn1, Δn2)

def simple_trans(simple_refl, α: NDArray[float64], n1:float=1, n2:float=1, uncertainty=False, Δα=0, Δn1=0, Δn2=0):
    def simple_trans_inner(R):
        return (1-R)**2

    R, ΔR = simple_refl(α, n1, n2, uncertainty, Δα, Δn1, Δn2)
    
    return GetResultAndUncertainty(simple_trans_inner, [R], uncertainty, [ΔR])

def simple_trans_p(α: NDArray[float64], n1:float=1, n2:float=1, uncertainty=False, Δα=0, Δn1=0, Δn2=0):
    return simple_trans(simple_refl_p, α, n1, n2, uncertainty, Δα, Δn1, Δn2)

def simple_trans_s(α: NDArray[float64], n1:float=1, n2:float=1, uncertainty=False, Δα=0, Δn1=0, Δn2=0):
    return simple_trans(simple_refl_s, α, n1, n2, uncertainty, Δα, Δn1, Δn2)