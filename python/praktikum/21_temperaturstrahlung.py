from matplotlib import pyplot as plt
from numpy import array
from tools.statistics.linear_regression import ScatterWithErrorBars, PlotLinregWithErrorAndScatterErrorbarsLogarithmic
from tools.maths.functions import Mean, Ratio

def Ex31_leslie():
    ΔT = 0.1
    T = array([86.1, 84.9, 84]) + 273.15
    ΔU_rel = .1
    black = array([.337, .335, .33])   # V
    mirror = array([.1, .1, .099])
    white = array([.335, .33, .325])
    dull = array([.105, .105, .077])

    black_ratio = array([1, 1, 1])
    mirror_ratio, Δmirror_ratio = Ratio(black, mirror, uncertainty=True, Δdenominator=black*ΔU_rel, Δnumerator=mirror*ΔU_rel)
    white_ratio, Δwhite_ratio = Ratio(black, white, uncertainty=True, Δdenominator=black*ΔU_rel, Δnumerator=white*ΔU_rel)
    dull_ratio, Δdull_ratio = Ratio(black, dull, uncertainty=True, Δdenominator=black*ΔU_rel, Δnumerator=dull*ΔU_rel)
    ax = plt.subplot()

    ScatterWithErrorBars(ax, T, black_ratio, ΔT, black_ratio*ΔU_rel, scatter_label="Schwarze Fläche", fmt="k.")
    ScatterWithErrorBars(ax, T, mirror_ratio, ΔT, Δmirror_ratio, scatter_label="Verspigelte Fläche", fmt="c.")
    ScatterWithErrorBars(ax, T, white_ratio, ΔT, Δwhite_ratio, scatter_label="Weiße Fläche", fmt="w.")
    ScatterWithErrorBars(ax, T, dull_ratio, ΔT, Δdull_ratio, scatter_label="Matte Fläche", fmt="b.", title="Verhältnisse der Strahlungsleistung zur schwarzen Fläche", xlabel="Temperatur / [K]", ylabel="Verhältnis")

def Ex32_r2_dependency():
    d = array([25, 30, 35, 40, 45, 50])*1e-2
    Δd = 0.5e-2
    ΔU_rel = .1
    PT100 = array([128.9, 129.1])
    T = array([347.7, 348.3]) # Mapped from PT100 values with a table
    U = array([[1.11, 0.81, 0.635, 0.51, 0.415, 0.35],
                [1.120, .815, .635, .505 ,.415, .345]])

    _, axs = plt.subplots(2, 1)
    coeffs = []
    covs = []
    for u, t, ax in zip(U, T, axs):
        coeff, cov = PlotLinregWithErrorAndScatterErrorbarsLogarithmic(ax, d, u, Δd, ΔU_rel*u, rf'Gemessen bei ${t}°C$', xlabel=r'$ln(d)$', ylabel=r'$ln(u)$')
        coeffs.append(coeff[0])
        covs.append(cov[0][0])

    inclination, Δinclination = Mean(coeffs, uncertainty=True, Δarr=covs)
    print(f"Inclination: {inclination} +/- {Δinclination}")

def Ex33_coolingBoltzmann():
    pass

def Ex34_pyroBoltzmann():
    pass

# Ex31_leslie()
Ex32_r2_dependency()

plt.tight_layout()
plt.show()