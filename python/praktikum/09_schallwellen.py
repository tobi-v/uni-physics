from matplotlib import pyplot as plt
from numpy import pi, zeros_like
from os.path import dirname, join
from pandas import read_csv
from tools.maths.functions import inverse
from tools.statistics.linear_regression import PlotLinregWithErrorAndScatterErrorbars
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

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

fig, axs = plt.subplots(2, 1)
sound_in_gases('air_data.csv', "Luft", axs[0])
sound_in_gases('co2_data.csv', "CO_2", axs[1])
plt.tight_layout()

plt.show()