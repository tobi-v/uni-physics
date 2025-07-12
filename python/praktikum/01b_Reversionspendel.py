from numpy import array, diag, linspace, max, mean, min, pi, sqrt, std
from tools.statistics.linear_regression import linreg
import matplotlib.pyplot as plt

# 1. Time calibration

T = array([86.417, 86.387, 86.390, 86.381, 86.378])
T_mean = mean(T)
T_uncertainty = sqrt(std(T/50))

# 2.
#length = array([74.6, 75, 75.6, 76, 76.8, 77.7, 78.3])*10**-2
#T_heavy_bottom  = array([T_mean, 86.671, 86.966, 87.204, 87.646, 88.226, 88.45])
#T_heavy_top     = array([86.737, 84.809, 86.979, 88.685, 87.548, 87.910, 87.99])
length = array([74.6, 75.6, 76.8, 77.7, 78.3])*10**-2
T_heavy_bottom  = array([T_mean, 86.966, 87.646, 88.226, 88.45])/50
T_heavy_top     = array([86.737, 86.979, 87.548, 87.910, 87.99])/50

# linreg
hb_fun, _, hb_cov = linreg(length, T_heavy_bottom**2)
ht_fun, _, ht_cov = linreg(length, T_heavy_top**2)

print(f"{hb_cov}\n{ht_cov}")

# intersection
def intersection_with_uncertainty(m1, b1, cov1, m2, b2, cov2):
    """
    Berechne den Schnittpunkt x = (b2 - b1) / (m1 - m2) zweier linearer Fits,
    sowie die Unsicherheit auf diesen Schnittpunkt via Gaußscher Fehlerfortpflanzung.

    Parameter:
    - m1, b1: Steigung und Achsenabschnitt der ersten Geraden
    - cov1: 2x2 Kovarianzmatrix der ersten Geraden (m1, b1)
    - m2, b2: Steigung und Achsenabschnitt der zweiten Geraden
    - cov2: 2x2 Kovarianzmatrix der zweiten Geraden (m2, b2)

    Rückgabe:
    - x: Schnittpunkt auf der x-Achse
    - sigma_x: Unsicherheit des Schnittpunkts
    """
    delta_m = m1 - m2
    delta_b = b2 - b1

    # Mittelwert des Schnittpunkts
    x = delta_b / delta_m

    # Einzelne Varianzen und Kovarianzen
    var_m1, cov_m1b1, var_b1 = cov1[0,0], cov1[0,1], cov1[1,1]
    var_m2, cov_m2b2, var_b2 = cov2[0,0], cov2[0,1], cov2[1,1]
    print(f"{var_b1} {var_b2} {var_m1} {var_m2}")
    # Gaußsche Fehlerfortpflanzung für x = (b2 - b1) / (m1 - m2)
    sigma_x_squared = (
        (1 / delta_m)**2 * (var_b1 + var_b2) +
        (delta_b / delta_m**2)**2 * (var_m1 + var_m2)
    )
    print(f"{sqrt(sigma_x_squared)}")

    return x, sqrt(sigma_x_squared)

hb_slope, hb_offset = hb_fun.coefficients
ht_slope, ht_offset = ht_fun.coefficients
l_eff, l_eff_uncertainty = intersection_with_uncertainty(hb_slope, hb_offset, hb_cov, ht_slope, ht_offset, ht_cov)


print(f"Die reduzierte Pendellänge beträgt {l_eff*100} +/- {l_eff_uncertainty*100} cm")

T_schnitt = (hb_fun(l_eff)**0.5 + ht_fun(l_eff)**0.5)/2
g = 4 * pi**2 * l_eff / T_schnitt**2
g_uncertainty = g * sqrt((l_eff_uncertainty / l_eff)**2 + (2 * T_uncertainty / T_schnitt)**2)

print(f"g = {g} +- {g_uncertainty} m/s²")

# plot
x_fit = linspace(min(length), max(length), 100)
fig, ax = plt.subplots()
ax.plot(length, T_heavy_bottom**2, 'o', label='Schwer unten', color="C0")
ax.plot(length, T_heavy_top**2, 'o', label='Schwer oben', color="C1")
ax.plot(x_fit, hb_fun(x_fit), label='Fit unten', color="C0")
ax.plot(x_fit, ht_fun(x_fit), label='Fit oben', color="C1")
ax.axvline(l_eff, color='gray', linestyle='--', label=f'Schnitt: {l_eff:.4f} m')
ax.set_xlabel("l / m")
ax.set_ylabel("$T^2$ / s$^2$")
ax.set_title("Messkurven ohne Ausreißer")
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.show()
