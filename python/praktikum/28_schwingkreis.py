from numpy import array, diff, log, mean, ones, std
from numpy.typing import NDArray
from tools.maths.functions import Ratio
from tools.statistics.linear_regression import linreg, polyreg
from tools.python.checks import CheckLengths
from tools.python.plot import ScatterWithErrorBars
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty
from typing import Tuple

import matplotlib.pyplot as plt

def OpenLoopDamping(t: NDArray, U: NDArray):
  """Berechnet das logarithmische Dekrement und die Dämpfungskonstante eines offenen Schwingkreises.

  Args:
    t (array): Zeitpunkte der Messungen in Sekunden.
    U (array): Amplituden in Volt.

  Returns:
    damping (float): Dämpfungskonstante.
    damping_uncertainty (float): Unsicherheit der Dämpfungskonstante.
  """
  delta = log(U[:-1] / U[1:])
  
  T = diff(t)
  decrements = delta / T

  damping = mean(decrements)/2
  damping_uncertainty = std(decrements)/2

  return damping, damping_uncertainty

def plot_bode_measurements(omega: NDArray,
                           U_den: NDArray,
                           U_num: NDArray,
                           phi: NDArray,
                           U_num_uncertainty: float = 0,
                           U_den_uncertainty: float = 0,
                           phase_uncertainty: float = 0,
                           suptitle: str = "Bode Plot"):
    """Compact Bode plot: data + polynomial mag-fit and unwrap+MA phase smoothing."""
    voltage_ratio, voltage_ratio_uncertainty = GetResultAndUncertainty(
        Ratio, [U_den, U_num], uncertainty=True,
        uncertainty_params=[U_num_uncertainty, U_den_uncertainty]
    )

    fig, (axA, axP) = plt.subplots(2, 1, figsize=(6, 6))
    fig.suptitle(suptitle, fontsize=14, y=0.96)

    ScatterWithErrorBars(axA, omega, voltage_ratio, y_absErr=voltage_ratio_uncertainty,
                         label="Messwerte", xlabel="Kreisfrequenz ω (1/s)",
                         ylabel=r'Spannungsverhältnis Ausgang/Eingang', title="Amplitude")
    mag_fit, _, _ = polyreg(omega, voltage_ratio, 10)
    axA.plot(omega, mag_fit(omega), '--C1', label="Fit")
    axA.set_xscale('log'); axA.set_yscale('log'); axA.set_ylim(top=2); axA.legend()

    ScatterWithErrorBars(axP, omega, phi, y_absErr=phase_uncertainty,
                         label="Messwerte", xlabel="Kreisfrequenz ω (1/s)",
                         ylabel=r'Phasenverschiebung $\varphi\degree$', title="Phase")
    # unwrap phase, smooth with small moving average, convert back to degrees
    phi_fit, _, _ = polyreg(omega, phi, 10)
    axP.plot(omega, phi_fit(omega), '--C1', label='smoothed')
    axP.set_xscale('log'); axP.set_yscale('linear'); axP.legend()

    plt.tight_layout()
    
def resonance_frequency(omega: NDArray, U_source: NDArray, U_signal: NDArray) -> float:
    """Bestimmt die Resonanzfrequenz aus den Messdaten.

    Args:
        omega (NDArray): Kreisfrequenzen.
        U_source (NDArray): Quellspannungen.
        U_signal (NDArray): gemessene Spannungen.

    Returns:
        float: Resonanzfrequenz.
    """
    amplitude_ratio = U_signal/U_source
    min_idx = amplitude_ratio.argmin()
    return min_idx, omega[min_idx]

def resistance(U_R: float, U_Vorwiderstand: float, R_Vorwiderstand: float) -> float:
    """Berechnet den Widerstand im Schwingkreis.

    Args:
        U_R (float): Spannung am Widerstand.
        U_Vorwiderstand (float): Spannung am Vorwiderstand.
        R_Vorwiderstand (float): Widerstand des Vorwiderstands.

    Returns:
        float: Widerstand im Schwingkreis.
    """
    return (U_R / U_Vorwiderstand) * R_Vorwiderstand

def capacity_from_low_frequencies(omega: NDArray, U_R: NDArray, U_chain: NDArray) -> Tuple[float, float]:
    """Berechnet die Kapazität aus den Messdaten bei niedrigen Frequenzen.

    Args:
        omega (NDArray): Kreisfrequenzen.
        U_source (NDArray): Quellspannungen.
        U_signal (NDArray): gemessene Spannungen.

    Returns:
        float: Kapazität in Farad.
    """
    inv_amplitude_ratio = U_R / U_chain
    low_freq_indices = omega < 100
    _, inclination, inclination_uncertainty = linreg(omega[low_freq_indices], inv_amplitude_ratio[low_freq_indices])
    return inclination, inclination_uncertainty

def inductivity_from_high_frequencies(omega: NDArray, U_R: NDArray, U_chain: NDArray) -> Tuple[float, float]:
    """Berechnet die Induktivität aus den Messdaten bei hohen Frequenzen.

    Args:
        omega (NDArray): Kreisfrequenzen.
        U_source (NDArray): Quellspannungen.
        U_signal (NDArray): gemessene Spannungen.

    Returns:
        float: Induktivität in Henry.
    """
    amplitude_ratio = U_chain / U_R
    high_freq_indices = omega > 5000  # Beispielgrenze für hohe Frequenzen
    _, inclination, inclination_uncertainty = linreg(omega[high_freq_indices], amplitude_ratio[high_freq_indices])
    return inclination, inclination_uncertainty

t_uncertainty = 10**-6 # s
U_uncertainty = 2*10**-3 # V
R_Vorwiderstand = 80 # Ohm

### Teil 1 freie Schwingung
t = array([0, 90, 190, 280, 380, 470, 570, 660, 750, 850, 940, 1040, 1130, 1230, 1320, 1410, 1510, 1600, 1700, 1790, 1880, 1980, 2070])*10**-6
U = array([63.2, 59.2, 54.4, 51.2, 48, 43.2, 40, 38.4, 35.2, 34.4, 30.4, 28.8, 28, 25.6, 23.2, 21.6, 20.8, 20, 16.8, 16, 16, 14.4, 12.8])*10**-3
CheckLengths(t, U)

damping, damping_uncertainty = OpenLoopDamping(t, U)
print("Dämpfungskonstante:", damping, "±", damping_uncertainty, "1/s")

_, ax =  plt.subplots(1, 1)
ScatterWithErrorBars(ax, t, U, x_absErr=t_uncertainty, y_absErr=U_uncertainty, label="Amplitude", xlabel="Zeit (s)", ylabel="Spannung (V)", title="Freie Schwingung: Spannung über Zeit")
U_fun, _, _ = polyreg(t, U, 5)
ax.plot(t, U_fun(t), '--b', label="Fit")
ax.legend()

### Teil 2: Erzwungene Schwingung
omega = array([10, 15, 20, 30, 50, 70, 125, 250, 500,
  700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700,
               2500, 4000, 5500, 7500, 10000, 15000, 20000, 25000, 30000])
U_chain = array([3000, 3000, 2960, 2940, 2880, 2760, 2520, 2100, 1920,
  1440, 1420, 1420, 1420, 1400, 1400, 1400, 1400, 1400, 1400, 1400,
                 1440, 1500, 1600, 1720, 1860, 2080, 2140, 2800, 2820])*10**-3
U_R = array([96, 146, 184, 272, 420, 552, 792, 1040, 1170,
  944, 944, 952, 952, 952, 952, 952, 952, 952, 952, 952,
             944, 896, 840, 744, 616, 360, 192, 320, 528])*10**-3
phi = array([90, 86, 85, 78, 72, 70, 60, 40, 20,
  16.5, 13, 9, 6, 6, 4.5, 3, 1.5, 0, -1, -3,
             -12, - 20, -28, -35, -40, -38, 6, 56, 77]) # degree
CheckLengths(omega, U_chain, U_R, phi)

plot_bode_measurements(omega, U_R + U_chain, U_chain, phi, U_uncertainty, U_uncertainty, 2, suptitle="Bode Plot angeregter Schwingkreis")

omega_no_outliers = array([10, 15, 20, 30, 50, 70, 125, 250, 500,
  700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700,
               2500, 4000, 5500, 7500, 10000, 15000])
U_chain_no_outliers = array([3000, 3000, 2960, 2940, 2880, 2760, 2520, 2100, 1920,
  1440, 1420, 1420, 1420, 1400, 1400, 1400, 1400, 1400, 1400, 1400,
                 1440, 1500, 1600, 1720, 1860, 2080])*10**-3
U_R_no_outliers = array([96, 146, 184, 272, 420, 552, 792, 1040, 1170,
  944, 944, 952, 952, 952, 952, 952, 952, 952, 952, 952,
             944, 896, 840, 744, 616, 360])*10**-3
phi_no_outliers = array([90, 86, 85, 78, 72, 70, 60, 40, 20,
  16.5, 13, 9, 6, 6, 4.5, 3, 1.5, 0, -1, -3,
             -12, - 20, -28, -35, -40, -38]) # degree
CheckLengths(omega_no_outliers, U_chain_no_outliers, U_R_no_outliers, phi_no_outliers)

plot_bode_measurements(omega_no_outliers, U_R_no_outliers + U_chain_no_outliers, U_chain_no_outliers, phi_no_outliers, U_uncertainty, U_uncertainty, 2, suptitle="Bode Plot angeregter Schwingkreis ohne Ausreißer")

res_idx, res_freq = resonance_frequency(omega, U_chain + U_R, U_chain)
print("Resonanzfrequenz: ", res_freq, " 1/s")
R_chain, R_chain_uncertainty = GetResultAndUncertainty(
    resistance, [U_chain[res_idx], U_R[res_idx], R_Vorwiderstand], uncertainty=True,
    uncertainty_params=[U_uncertainty, U_uncertainty, 0])
print("Widerstand im Schwingkreis: ", R_chain, " +/- ", R_chain_uncertainty, " Ohm")
C_chain, C_chain_uncertainty = capacity_from_low_frequencies(omega_no_outliers, U_R_no_outliers, U_chain_no_outliers)
print("Kapazität im Schwingkreis: ", C_chain[0], " +/- ", C_chain_uncertainty[0][0], " F")
L_chain, L_chain_uncertainty = inductivity_from_high_frequencies(omega_no_outliers, U_R_no_outliers, U_chain_no_outliers)
print("Induktivität im Schwingkreis: ", L_chain[0], " +/- ", L_chain_uncertainty[0][0], " H")

### 3. 4-Pol

omega = array([10, 100, 1000, 5000, 6000, 6500, 7000, 7250, 7500, 7750, 8000, 8250, 8500, 8750, 9000, 9250, 9500, 9750, 10000, 10500, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 25000, 30000, 40000, 60000, 80000, 99990])
U_signal = array([3.36, 3.36, 3.36, 2.76, 2.56, 2.48, 2.4, 2.32, 2.32, 2.32, 2.24, 2.24, 2.16, 2.12, 2.08, 2.08, 2, 1.96, 1.92, 1.88, 1.8, 1.68, 1.6, 1.52, 1.44, 1.36, 1.28, 1.2, 1.16, 1.12, 0.92, 0.92, 0.72, 0.52, 0.44, 0.36])
phi = array([0, 1, -6, -33, -41, -42, -42, -44, -46, -46, -48, -49, -50, -50, -50, -52, -50, -51, -52, -54, -53, -60, -60, -60, -65, -65, -62, -67, -64, -70, -80, -66, -85, -60, -87, -90]) # degree
U_source = 4 * ones(len(omega))
CheckLengths(omega, U_source, U_signal, phi)

plot_bode_measurements(omega, U_source, U_signal,  phi, U_uncertainty, U_uncertainty, 2, suptitle="Bode Plot 4-Pol")

omega_no_outliers = array([10, 100, 1000, 5000, 6000, 6500, 7000, 7250, 7500, 7750, 8000, 8250, 8500, 8750, 9000, 9250, 9500, 9750, 10000, 10500, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 25000, 40000, 80000, 99990])
U_signal_no_outliers = array([3.36, 3.36, 3.36, 2.76, 2.56, 2.48, 2.4, 2.32, 2.32, 2.32, 2.24, 2.24, 2.16, 2.12, 2.08, 2.08, 2, 1.96, 1.92, 1.88, 1.8, 1.68, 1.6, 1.52, 1.44, 1.36, 1.28, 1.2, 1.16, 1.12, 0.92, 0.72, 0.44, 0.36])
phi_no_outliers = array([0, 1, -6, -33, -41, -42, -42, -44, -46, -46, -48, -49, -50, -50, -50, -52, -50, -51, -52, -54, -53, -60, -60, -60, -65, -65, -62, -67, -64, -70, -80, -85, -87, -90]) # degree
U_source_no_outliers = 4 * ones(len(omega_no_outliers))
CheckLengths(omega_no_outliers, U_source_no_outliers, U_signal_no_outliers, phi_no_outliers)

plot_bode_measurements(omega_no_outliers, U_source_no_outliers, U_signal_no_outliers,  phi_no_outliers, U_uncertainty, U_uncertainty, 2, suptitle="Bode Plot 4-Pol ohne Ausreißer")

plt.show()