from numpy import array, linspace
from tools.hydrodyn.static_properties import GravitationalPressure
from tools.statistics.linear_regression import linreg

import matplotlib.pyplot as plt

g = 9.81
rho = 1
h = 10
uncertainty = True

print(GravitationalPressure(rho, g, h, uncertainty))

# 1

h_cal = linspace(0, 15, 7)*1e-3
U_cal = array([240, 312, 408, 592, 752, 928, 1110])*1e-3 # V

p_params = linreg(U_cal, h_cal)

fig, ax = plt.subplots(3, 1)
ax[0].plot(h_cal, U_cal)

# Diameter kapillaren
uncertainty_caliper = 0.05e-3
d = array([1, 1.7, 2.95, 4.85])*1e-3

# Destilliertes Wasser

U_dest = array([2.42, 1, 0.49, 0.424]) # V
ax[1].plot(2/d, U_dest)
plt.show()

# Salzwasser

U_sal = array([2.32, 1.08, 0.616, 0.528])
ax[2].plot(2/d, U_dest)
plt.show()

# Dichtebestimmung

h_diff = 1.5e-2
U_salt = 1.18 # V
U_desti = 0.6