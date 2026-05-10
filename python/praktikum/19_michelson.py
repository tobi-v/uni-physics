from numpy import mean, std
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

def κ_fun(N, λ, Δx, uncertainty=False, delN=0, delλ=0, delΔx=0):
    def κ_inner(N, λ, Δx):
        Δs = N*λ / 2
        return Δs / Δx
    
    return GetResultAndUncertainty(κ_inner, [N, λ, Δx], uncertainty, [delN, delλ, delΔx])

def λ_fun(N, κ, Δx, uncertainty=False, delN=0, delκ=0, delΔx=0):
    def λ_inner(N, κ, Δx):
        return 2*κ*Δx/N
    
    return GetResultAndUncertainty(λ_inner, [N, κ, Δx], uncertainty, [delN, delκ, delΔx])

N = 200
N_σ = 10
Δx = [0.93, 0.995, 0.855]   # [mm]
Δx_μ = mean(Δx)
Δx_σ = std(Δx)
λ_laser = 532 # [nm]

print(f"Δx: {Δx_μ:.3f} ± {Δx_σ:.3f} mm")

κ, κ_σ = κ_fun(N, λ_laser, Δx_μ, uncertainty=True, delN=N_σ, delλ=0, delΔx=Δx_σ)

print(f"κ: {κ:.4f} ± {κ_σ:.4f}")

Δx_dampflampe = [0.96, 0.99, 0.97]   # [mm]
Δx_dampflampe_μ = mean(Δx_dampflampe)
Δx_dampflampe_σ = std(Δx_dampflampe)
λ_dampflampe, λ_dampflampe_σ = λ_fun(N, κ, Δx_dampflampe_μ, uncertainty=True, delN=N_σ, delκ=κ_σ, delΔx=Δx_dampflampe_σ)

print(f"λ_dampflampe: {λ_dampflampe:.4f} ± {λ_dampflampe_σ:.4f} nm")