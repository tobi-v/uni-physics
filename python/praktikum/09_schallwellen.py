from matplotlib import pyplot as plt
from numpy import array, ones_like, zeros_like
from os.path import dirname, join
from pandas import read_csv
from tools.maths.functions import inverse
from tools.statistics.linear_regression import PlotLinregWithErrorAndScatterErrorbars
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty
from tools.waves.standing_waves import λ_caseA, λ_caseB

Δs = 0.1 # [cm]

def read(file):
    script_dir = dirname(__file__)
    csv_path = join(script_dir, file)
    data = read_csv(csv_path)
    return data

def λ_from_maxima(s_u, s_o, n):
    def λ_from_maximaInner(s_u, s_o, n):
        return 2*(s_o - s_u) / n
    
    return GetResultAndUncertainty(λ_from_maximaInner, [s_u, s_o, n], uncertainty=True, uncertainty_params=[Δs, Δs, 0])

def sound_in_gases(file, medium, ax):
    data = read(join('09_data', file))
    freqs = data['f'].to_numpy()
    s_u = data['s_u'].to_numpy()
    s_o = data['s_o'].to_numpy()
    n = data['n'].to_numpy()

    λ, Δλ = λ_from_maxima(s_u, s_o, n)
    λ_inv, Δλ_inv = inverse(λ, uncertainty=True, Δx=Δλ)

    coeff, cov = PlotLinregWithErrorAndScatterErrorbars(ax, 100*λ_inv, freqs, 100*Δλ_inv, zeros_like(freqs),
                                           f"Frequenz und inverse Wellenlänge in {medium}",
                                           xlabel=r'$\frac{1}{\lambda}$', ylabel=r'$f$')
    print(f'In {medium}: c={coeff[0]:.2f} ± {cov[0][0]**.5:.2f} m/s')

def sound_in_metals():
    L = 115e-2 # [m]
    ΔL = 0.5e-2
    
    fig, axs = plt.subplots(2, 1)

    # Locked in the middle
    peaks01 = array([2, 6.2, 10.4])*1e3    # Hz TODO: SET UNCERTAINTY FOR FREQUENCY
    modes01 = array([1, 2, 3])
    λ01, Δλ01 = λ_caseA(L*ones_like(modes01), modes01, uncertainty=True, Δlength=ΔL)

    coeff, cov = PlotLinregWithErrorAndScatterErrorbars(axs[0], λ01, peaks01, Δλ01, zeros_like(peaks01),
                                                        f"Maul halten bitte")

    # Locked at 1/4 and 3/4
    peaks02 = array([1.25, 4.125, 8.25])
    modes02 = array([1, 2, 4])
    λ02, Δλ02 = λ_caseB(L, modes02, uncertainty=True, Δlength=ΔL)

    plt.tight_layout()

fig, axs = plt.subplots(2, 1)
sound_in_gases('air_data.csv', "Luft", axs[0])
sound_in_gases('co2_data.csv', r"$\text{CO}_\text{2}$", axs[1])
plt.tight_layout()

sound_in_metals()

plt.show()