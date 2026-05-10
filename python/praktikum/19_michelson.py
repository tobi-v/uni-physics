from numpy import mean, std
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

def κ_fun(N, λ, Δx, uncertainty=False, delN=0, delλ=0, delΔx=0):
    def κ_inner(N, λ, Δx):
        Δs = N*λ / 2
        return Δs / Δx
    
    return GetResultAndUncertainty(κ_inner, [N, λ, Δx], uncertainty, [delN, delλ, delΔx])

N = 200
N_σ = 10
xs = [0.93, 0.995, 0.855]   # [mm]
Δx_μ = mean(xs)
Δx_σ = std(xs)
λ = 532e-6  # [mm]

print(f"Δs: {Δx_μ:.3f} ± {Δx_σ:.3f} mm")

κ, κ_σ = κ_fun(N, λ, Δx_μ, uncertainty=True, delN=N_σ, delλ=0, delΔx=Δx_σ)

print(f"κ: {κ:.4f} ± {κ_σ:.4f}")