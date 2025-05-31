from numpy import array, empty, linspace, sqrt
from tools.hydrodyn.static_properties import GravitationalPressure, RhoFromGravitationalPresure
from tools.statistics.linear_regression import linreg, plotWithErrorBars
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

import matplotlib.pyplot as plt

fig, axs = plt.subplots(3, 1)
textbox_props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

g   = 9.81  # [m/s^2]
rho = 997   # [kg/m^3]

uncertainty         = True
uncertainty_caliper = 0.05e-3   # [m]
uncertainty_osci    = 2e-3      # [m]
 
d = array([1, 1.7, 2.95, 4.85])*1e-3 # [m] Diameter capillaries

### 1. Calibration of measurement device

h_cal = linspace(0, 15, 7)*1e-3                             # [m]
U_cal = array([240, 312, 408, 592, 752, 928, 1110])*1e-3    # [V]
p_cal = GravitationalPressure(rho, g, h_cal)                # [Pa]

U_to_p, U_to_p_coeffs, U_to_p_cov = linreg(U_cal, p_cal)

plotWithErrorBars(axs[0], U_cal, p_cal,  U_to_p,
                  x_absErr=uncertainty_osci, y_absErr=uncertainty_caliper,
                  title="Kalibrierung des Messgerätes", xlabel=r'Spannung $[V]$', ylabel=r'Druckdifferenz $[Pa]$')
measurement_device_textbox = r'$p \propto %.1f\cdot U$' % U_to_p_coeffs[0]
axs[0].text(0.05, 0.95, measurement_device_textbox, transform=axs[0].transAxes, fontsize=14, verticalalignment='top', bbox=textbox_props)

### 2. Distilled Wasser

def GetSigmaFromPressure(r: array, p: array):
    fun, coeffs, cov = linreg(1/r, p)
    sigma = coeffs[0]/2
    sigma_deviation = sqrt(cov[0,0])/2
    return fun, sigma, sigma_deviation

def ProcessResultsFromVoltage(U: array, substance: str, ax):
    p = U_to_p(U)
    fun, sigma, sigma_deviation = GetSigmaFromPressure(d/2, p)
    plotWithErrorBars(ax, 2/d, p, fun,
                      x_absErr=0, y_absErr=sigma_deviation,
                      title=f"Messung für {substance}", xlabel=r'1/r $[\frac{1}{m}]$', ylabel=r'Druckdifferenz $[Pa]$')
    print(f"\nFür {substance}: \tsigma = ({sigma/2:1.5f} +/- {sigma_deviation:1.5f}) N/m")

print(f"Literaturwert destilliertes Wasser: sigma = {72.75e-3} N/m")
U = array([2.42, 1, 0.49, 0.424]) # [V] Measured voltages for distilled water
ProcessResultsFromVoltage(U, "demineralisiertes Wasser", axs[1])

### 3. Saltwater

U_sal = array([2.32, 1.08, 0.616, 0.528]) # [V] Measured voltages for saltwater
ProcessResultsFromVoltage(U_sal, "Salzwasser", axs[2])


### 4. Density

h_diff = 1.5e-2 # [m]
U_desti = 0.6   # [V]
U_salt = 1.18   # [V]

p_desti, p_desti_uncertainty = GetResultAndUncertainty(U_to_p, U_desti, uncertainty, uncertainty_params=uncertainty_osci)
p_salt, p_salt_uncertainty = GetResultAndUncertainty(U_to_p, U_salt, uncertainty, uncertainty_params=uncertainty_osci)

rho_desti, rho_desti_deviation = RhoFromGravitationalPresure(p_desti, g, h_diff, uncertainty, delP=p_desti_uncertainty, delG=0, delH=uncertainty_caliper)
rho_salt, rho_salt_deviation = RhoFromGravitationalPresure(p_salt, g, h_diff, uncertainty, delP=p_salt_uncertainty, delG=0, delH=uncertainty_caliper)

print(f"Dichte von destilliertem Wasser: rho = ({rho_desti:1.1f} +/- {rho_desti_deviation}) kg/m^3")
print(f"Dichte von Salzwasser: rho = ({rho_salt:1.1f} +/- {rho_salt_deviation}) kg/m^3")

plt.tight_layout()
plt.show()