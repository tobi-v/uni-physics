import matplotlib.pyplot as plt
from numpy import arange, array, exp, linspace, log, mean, pi, sqrt, std
from scipy.optimize import curve_fit
from scipy.stats import linregress
from tools.dynamics.harmonic_osci import estimate_damping_constant, find_resonance_frequency
from tools.maths.functions import gaussian
from tools.python.sort import sort_by_x_and_filter_unique
from tools.statistics.linear_regression import Linreg, Polyreg

### 1. Gedämpfte Schwingungen

# Periodendauern [s]
T396 = 1.575
T200 = 1.6875
T9   = 1.989

t396 = array([1.97, 1.21, 0.761, 0.47, 0.291])
t200 = array([2.71, 2.35, 1.99, 1.72, 1.48, 1.28, 1.10, 0.94, 0.828, 0.716, 0.604])
t9   = array([1.57, 1.53, 1.46, 1.39, 1.35, 1.30, 1.23, 1.21, 1.16, 1.09, 1.07])

# Dämpfungskonstanten aus dem Kurvenverlauf
δ396_est  = estimate_damping_constant(T396*arange(0, len(t396)), t396)
δ200_est  = estimate_damping_constant(T200*arange(0, len(t200)), t200)
δ9_est  = estimate_damping_constant(T9*arange(0, len(t9)), t9)
print("\n### Versuchsteil 1: Gedämpfte Schwingungen ###\n")
print(f"Für 396 mA: Dämpfungskonstante aus Kurvenverlauf δ = {δ396_est:.4f} 1/s")
print(f"Für 200 mA: Dämpfungskonstante aus Kurvenverlauf δ = {δ200_est:.4f} 1/s")
print(f"Für   9 mA: Dämpfungskonstante aus Kurvenverlauf δ = {δ9_est:.4f}   1/s")

def log_dekrement(amplituden):
    return mean(log(amplituden[:-1] / amplituden[1:]))

Λ396 = log_dekrement(t396)
Λ200 = log_dekrement(t200)
Λ9   = log_dekrement(t9)

# Dämpfungskonstanten δ = Λ / T
δ396 = Λ396 / T396
δ200 = Λ200 / T200
δ9   = Λ9 / T9

print(f"\nFür 396 mA: Dämpfungskonstante δ = {δ396:.4f} 1/s \t\tLogarithmisches Dekrement Λ = {Λ396:.4f}")
print(f"Für 200 mA: Dämpfungskonstante δ = {δ200:.4f} 1/s \t\tLogarithmisches Dekrement Λ = {Λ200:.4f}")
print(f"Für   9 mA: Dämpfungskonstante δ = {δ9:.4f}   1/s   \tLogarithmisches Dekrement Λ = {Λ9  :.4f}")

# Plot mit exp fit
x396 = T396 * array(range(len(t396)))
x200 = T200 * array(range(len(t200)))
x9   = T9   * array(range(len(t9)))
def exp_decay(t, A0, δ):
    return A0 * exp(-δ * t)

fig1, ax1 = plt.subplots(1, 1, figsize=(8, 5))

for label, t, x, δ, color in [
    ("396 mA", t396, x396, δ396, "C0"),
    ("200 mA", t200, x200, δ200, "C1"),
    ("9 mA",   t9,   x9,   δ9,   "C2")
]:
    # Fit A0 only, fix δ
    popt, _ = curve_fit(lambda t, A0: exp_decay(t, A0, δ), x, t, p0=(t[0],))
    t_fit = linspace(0, max(x), 300)
    ax1.plot(x, t, 'o', label=f"{label} data", color=color)
    ax1.plot(t_fit, exp_decay(t_fit, *popt, δ), '-', label=f"{label} fit", color=color)

ax1.set_xlabel("Zeit [s]")
ax1.set_ylabel("Amplitude [V]")
ax1.set_title("Exponentieller Abfall der gedämpften Oszillation")
ax1.legend()
ax1.grid(True)

### 2. Erzwungene Schwingungen
print("\n### Versuchsteil 2: Erzwungene Schwingungen ###\n")

def damping_from_phase_shift(current, omega, phi):
  slope, _, _, _, _ = linregress(omega, phi)
  beta = -1/slope
  print(f"Dämpfung für {current} mA: beta = {beta} 1/s")  

def print_damping_and_resonance(current, omega, phi, ampl):
    damping_from_phase_shift(current, omega, phi)
    omega_sorted, ampl_sorted = sort_by_x_and_filter_unique(omega, ampl)
    res_freq = find_resonance_frequency(omega_sorted, ampl_sorted)
    print(f"Bei einer Dämpfung von {current} mA liegt die Resonanz bei omega = {res_freq} Hz")

# Widerstand: 253 mA
current251 = 251 # [mA]
omega251 = array([ # [Hz]
    432, 455, 474, 483, 495, 504, 508, 520, 523, 530,
    537, 545, 564, 596, 536, 513, 480, 497, 504, 498])/10**3
ampl251 = array([ # [V]
    649.6, 851.2, 1277, 1770, 2350, 2554, 2352, 1949, 1635, 1344,
    1142, 963.2, 649.6, 425.6, 1120, 2083, 1635, 2464, 2554, 2531])/10**3
phi251 = array([ # [radian]
    14.7, 17.61, 28.5, 41.47, 63.9, 94.2, 115.5, 131.6, 142, 148.1,
    152.2, 159.2, 165.3, 172.4, 154.6, 129, 32, 69.4, 96.1, 72.9])*pi/180
   
print_damping_and_resonance(current251, omega251, phi251, ampl251)

# Widerstand: 401 mA
current401 = 401 # [mA]
omega401 = array([ # [Hz]
    499, 516, 545, 551, 565, 436, 454, 464, 469, 482,
    497, 509, 525, 518, 512, 526, 532, 541, 551, 558])/10**3
ampl401 = array([ # [V]
    1142, 1053, 784.0, 672.0, 560.0, 582.4, 694.4, 828.8, 918.4, 1030,
    1142, 1120, 963.2, 1030, 1075, 1008, 851.2, 761.6, 672.0, 627.2])/10**3
phi401 = array([ # [radian]
    88.9, 108.1, 129.3, 136.1, 141.4, 24.4, 36.1, 42.7, 52.4, 62.6,
    79.1, 97.2, 118, 110.1, 105.4, 115.4, 129.4, 134.1, 136.8, 140.3])*pi/180

print_damping_and_resonance(current401, omega401, phi401, ampl401)

fig2, ax2 = plt.subplots(1, 1, figsize=(8, 5))
fig3, ax3 = plt.subplots(1, 1, figsize=(8, 5))

for label, omega, ampl, phi, color in [
    ("251 mA", omega251, ampl251, phi251, "C0"),
    ("401 mA", omega401, ampl401, phi401, "C1")
]:
    phi_deg = -phi*180/pi
    fit, _, _ = Linreg(omega, phi_deg)
    cubic_fit, _, _ = Polyreg(omega, phi_deg, 3)
    ax2.plot(omega, phi_deg, 'o', label=f"{label} data", color=color)
    ax2.plot(omega, fit(omega), '-', label=f"{label} linear fit", color=color)
    omega_fit = linspace(min(omega), max(omega), 300)
    ax2.plot(omega_fit, cubic_fit(omega_fit), '-', label=f"{label} cubic fit", color=color)

    initial_guess = [max(omega), mean(omega), std(omega)]
    popt, pcov = curve_fit(gaussian, omega, ampl, p0=initial_guess)
    _, gaussmean, stddev = popt
    halbwertsbreite = 2 * sqrt(2 * log(2)) * stddev
    ax3.scatter(omega, ampl, label=f"{label} data")
    ax3.plot(omega_fit, gaussian(omega_fit, *popt), label=f"{label} Gaussian fit", color=color)
    plt.axvline(gaussmean - halbwertsbreite/2, color=color, linestyle='--', label=f"{label} Halbwertsbreite")
    plt.axvline(gaussmean + halbwertsbreite/2, color=color, linestyle='--')
    print(f"Halbwertsbreite bei {label}: {halbwertsbreite} [Hz]")

ax2.set_xlabel("Frequenz [1/s]")
ax2.set_ylabel("Phasenverschiebung [deg]")
ax2.set_title("Phasenverschiebung in Abhängigkeit von der Anregungsfrequenz")
ax2.legend()
ax2.grid(True)
ax3.set_xlabel("Frequenz [1/s]")
ax3.set_ylabel("Amplitude [V]")
ax3.set_title("Amplitude in Abhängigkeit von der Anregungsfrequenz")
ax3.legend()
ax3.grid(True)

# Show the plots
plt.tight_layout()
plt.show()