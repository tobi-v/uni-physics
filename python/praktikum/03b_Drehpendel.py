import matplotlib.pyplot as plt
from numpy import argmax, array, exp, linspace, log, mean, pi
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
from scipy.stats import linregress

### 1. Gedämpfte Schwingungen

# Periodendauern [s]
T396 = 1.575
T200 = 1.6875
T9   = 1.989

t396 = array([1.97, 1.21, 0.761, 0.47, 0.291])
t200 = array([2.71, 2.35, 1.99, 1.72, 1.48, 1.28, 1.10, 0.94, 0.828, 0.716, 0.604])
t9   = array([1.57, 1.53, 1.46, 1.39, 1.35, 1.30, 1.23, 1.21, 1.16, 1.09, 1.07])
# TODO Get damping constants from estimate_damping_constant
def log_dekrement(amplituden):
    return mean(log(amplituden[:-1] / amplituden[1:]))

Λ396 = log_dekrement(t396)
Λ200 = log_dekrement(t200)
Λ9   = log_dekrement(t9)

# Dämpfungskonstanten δ = Λ / T
δ396 = Λ396 / T396
δ200 = Λ200 / T200
δ9   = Λ9 / T9

# Ausgabe
print("\n### Versuchsteil 1: Gedämpfte Schwingungen ###\n")
print(f"Für 396 mA: Dämpfungskonstante δ = {δ396:.4f} 1/s \t\tLogarithmisches Dekrement Λ = {Λ396:.4f}")
print(f"Für 200 mA: Dämpfungskonstante δ = {δ200:.4f} 1/s \t\tLogarithmisches Dekrement Λ = {Λ200:.4f}")
print(f"Für   9 mA: Dämpfungskonstante δ = {δ9:.4f}   1/s   \tLogarithmisches Dekrement Λ = {Λ9  :.4f}")

# Plot mit exp fit
x396 = T396 * array(range(len(t396)))
x200 = T200 * array(range(len(t200)))
x9   = T9   * array(range(len(t9)))
def exp_decay(t, A0, δ):
    return A0 * exp(-δ * t)

fig, ax = plt.subplots(1, 1, figsize=(8, 5))

for label, t, x, δ, color in [
    ("396 mA", t396, x396, δ396, "C0"),
    ("200 mA", t200, x200, δ200, "C1"),
    ("9 mA",   t9,   x9,   δ9,   "C2")
]:
    # Fit A0 only, fix δ
    popt, _ = curve_fit(lambda t, A0: exp_decay(t, A0, δ), x, t, p0=(t[0],))
    t_fit = linspace(0, max(x), 300)
    ax.plot(x, t, 'o', label=f"{label} data", color=color)
    ax.plot(t_fit, exp_decay(t_fit, *popt, δ), '-', label=f"{label} fit", color=color)

ax.set_xlabel("Zeit [s]")
ax.set_ylabel("Amplitude [V]")
ax.set_title("Exponentieller Abfall der gedämpften Oszillation")
ax.legend()
ax.grid(True)

### 2. Erzwungene Schwingungen
print("\n### Versuchsteil 2: Erzwungene Schwingungen ###\n")

def daempfung(current, omega, phi):
  slope, _, _, _, _ = linregress(omega, phi)
  beta = -1/slope
  print(f"Dämpfung für {current} mA: beta = {beta} 1/s")

def resonance(current, omega, amplitude):# TODO: Replace with find_resonance_frequency
  peaks, _ = find_peaks(omega, amplitude)
  print(f"Peak für Dämpfung von {current} mA at amplitude of omega = {omega[argmax(amplitude)]} Hz")

# Widerstand: 253 mA
current = 251 # [mA]
omega = array([ # [Hz]
    432, 455, 474, 483, 495, 504, 508, 520, 523, 530,
    537, 545, 564, 596, 536, 513, 480, 497, 504, 498])/10**3
ampl = array([ # [V]
    649.6, 851.2, 1277, 1770, 2350, 2554, 2352, 1949, 1635, 1344,
    1142, 963.2, 649.6, 425.6, 1120, 2083, 1635, 2464, 2554, 2531])/10**3
phi = array([ # [radian]
    14.7, 17.61, 28.5, 41.47, 63.9, 94.2, 115.5, 131.6, 142, 148.1,
    152.2, 159.2, 165.3, 172.4, 154.6, 129, 32, 69.4, 96.1, 72.9])*pi/180

daempfung(current, omega, phi)
resonance(current, omega, ampl)
# TODO Plot

# Widerstand: 401 mA
current = 401 # [mA]
omega = array([ # [Hz]
    499, 516, 545, 551, 565, 436, 454, 464, 469, 482,
    497, 509, 525, 518, 512, 526, 532, 541, 551, 558])/10**3
ampl = array([ # [V]
    1142, 1053, 784.0, 672.0, 560.0, 582.4, 694.4, 828.8, 918.4, 1030,
    1142, 1120, 963.2, 1030, 1075, 1008, 851.2, 761.6, 672.0, 627.2])/10**3
phi = array([ # [radian]
    88.9, 108.1, 129.3, 136.1, 141.4, 24.4, 36.1, 42.7, 52.4, 62.6,
    79.1, 97.2, 118, 110.1, 105.4, 115.4, 129.4, 134.1, 136.8, 140.3])*pi/180

daempfung(current, omega, phi)
resonance(current, omega, ampl)

# Ahoq rhw plots
plt.tight_layout()
plt.show()