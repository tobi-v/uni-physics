from matplotlib import pyplot as plt
from numpy import append, argsort, argmax, array, mean, pi, sqrt, std, where
from os.path import dirname, join
from pandas import read_csv
from tools.maths.functions import Product
from tools.signals.fourier import fft
from tools.statistics.linear_regression import Linreg, PlotLinregWithErrorAndScatterErrorbars, Polyreg, ScatterWithErrorBars
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

g = 9.81

threshold = 1.5
subsignal_length = 8

def load_data(file):
    script_dir = dirname(__file__)
    csv_path = join(script_dir, file)
    return read_csv(csv_path, delimiter="\t", skiprows=3)

def calibration():
    masses = array([0, 0.5, 1.0, 2.0])
    filenames = ['Kalibrierung-0.csv', 'Kalibrierung-0_5.csv', 'Kalibrierung-1_0.csv', 'Kalibrierung-2_0.csv']

    V_means = array([])
    V_stds = array([])
    for m, file in zip(masses, filenames):
        electric_signal = load_data(file)
        V_mean = electric_signal['Voltage (V)'].mean()
        V_std = electric_signal['Voltage (V)'].std()

        #print(f"Masse m={m} kg, Spannung U={V_mean:.4f} ± {V_std:.4f}")

        V_means = append(V_means, V_mean)
        V_stds = append(V_stds, V_std)

    fun, coeff, cov = Linreg(V_means, masses * g)
    #print(f"Die Kennlinie des Messgerätes für Spannung auf Kraft ist ({coeff[0]:.2f} ± {sqrt(cov[0][0]):.2f})x + ({coeff[1]:.2f} ± {sqrt(cov[1][1]):.2f})")

    return fun, coeff, cov

def ω_to_force(fun):
    filenames = [f'{name}_{ii}' for name in ('Petros', 'Tobi') for ii in range(1, 5)]

    freq_fig, freq_axs = plt.subplots(4, 2)
    ω_means = []
    Δωs = []
    F_means = []
    ΔFs = []
    for file, ax in zip(filenames, freq_axs.flatten()):
        data = load_data(f'{file}.csv')
        t = data['Time (s)'].to_numpy()
        U = data['Ch.1 (V)']
        ω = data['Ch.2 (V)'].to_numpy()

        freqs, ω_ft = fft(t, ω)
        freqs = freqs/subsignal_length # divide by number of magnets on the wheel
        mask = freqs < 5; freqs = freqs[mask]; ω_ft = ω_ft[mask]
        max_f = freqs[argmax(ω_ft)]
        ax.plot(freqs, ω_ft, color='k')
        ax.axvline(max_f, color='r', linestyle='--', label=f"Maximum bei {max_f:.1f} Hz")
        ax.set_title(file)
        ax.set_xlabel('ω / Hz')
        ax.set_ylabel('amplitude')
        ax.legend()

        rising_edges = where((ω[:-1]<threshold) & (ω[1:] >= threshold))[0]

        subsignals = []
        subsignals_t = []
        freqs2 = []
        for ii in range(0, len(rising_edges) - subsignal_length + 1):
            start_idx = rising_edges[ii]; end_idx = rising_edges[ii + subsignal_length - 1]
            subsignals.append(ω[start_idx:end_idx])
            subsignals_t.append(t[start_idx:end_idx])
            freqs2.append(1/(t[end_idx] - t[start_idx]))
        Δf = std(freqs2)

        print(f"{file}: f = {mean(freqs2):.3f} ± {std(freqs2):.3f} over n={len(freqs2)} subsignals")

        U_mean = U.mean()
        ΔU = U.std()

        F, ΔF = GetResultAndUncertainty(fun, [U_mean], uncertainty=True, uncertainty_params=[ΔU])
        ax.text(0.74, 0.45, f"F = {F:.1f} ± {ΔF:.1f} N", transform=ax.transAxes,
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='k'))
        # print(f"{file}: F = {F:.1f} ± {ΔF:.1f} N")

        ω_means.append(max_f)#*2*pi)
        Δωs.append(Δf)#*2*pi)
        F_means.append(F)
        ΔFs.append(ΔF)

    plt.tight_layout()
    Ff_fig, Ff_ax = plt.subplots()
    # ω_means = array(ω_means)
    # F_means = array(F_means)
    # Δωs = array(Δωs)
    # ΔFs = array(ΔFs)
    # order = argsort(ω_means)
    # ω_means = ω_means[order]
    # F_means = F_means[order]
    # Δωs = Δωs[order]
    # ΔFs = ΔFs[order]
    coeff, cov = PlotLinregWithErrorAndScatterErrorbars(Ff_ax, ω_means, F_means, Δωs, ΔFs, "Frequenz und Kraft", "Kreisfrequenz [Hz]", "Kraft [N]")
    print(f"Übertragungsfunktion: F(ω) = ({coeff[0]:.1f} ± {cov[0][0]:.1f}) ω + ({coeff[1]:.1f} ± {cov[1][1]:.1f})")

    plt.subplots_adjust(hspace=0.75)
    #plt.close(Ff_fig)
    plt.close(freq_fig)

    return ω_means, F_means, Δωs, ΔFs

def ω_to_power(ω, F, Δω, ΔF):
    R_bremsrad = 63e-3  # [m]
    ΔR_bremsrad = .5e-3

    P = []; ΔP = []
    for _F, _ω, _ΔF, _Δω in zip(F, ω, ΔF, Δω):
        p, Δp = Product([_F, _ω, R_bremsrad], uncertainty=True, Δarr=[_ΔF, _Δω, ΔR_bremsrad])
        P.append(p); ΔP.append(Δp)
        print(f"P = {p:.2f} ± {Δp:.2f} W")

    fig, ax = plt.subplots()
    ScatterWithErrorBars(ax, ω, P, Δω, ΔP, "Frequenz und Leistung", scatter_label="Datenpunkte")
    ax.set_xlabel("Kreisfrequenz [Hz]", size='18')
    ax.set_ylabel("Leistung [W]", size='18')

    fun, coeff, cov = Polyreg(ω, P, order=2)
    ω = array(ω)
    P = array(P)
    order = argsort(ω)
    ω = ω[order]
    P = P[order]
    ax.plot(ω, fun(ω), '--k', label="Regressionskurve")
    print(f"P(ω) = ({coeff[0]:.4f} ± {cov[0][0]:.4f}) ω² + ({coeff[1]:.2f} ± {cov[1][1]:.2f}) ω + ({coeff[2]:.1f} ± {cov[2][2]:.1f})")
    ax.legend()

    #plt.close(fig)

fun, coeff, cov = calibration()
ω, F, Δω, ΔF = ω_to_force(fun)
ω_to_power(ω, F, Δω, ΔF)

plt.tight_layout()
plt.show()

