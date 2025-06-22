from matplotlib import pyplot as plt
from numpy import array, log
from scipy.stats import linregress

T = array([ 25, 30,   35,   40,   45,   50,   55])+273.15       # [K]
mu = array([50, 42.2, 36.6, 30.2, 25.4, 21.9, 18.8])*1e-3     # [Pa s]
x = 1/T
y = log(mu)

# Linear fit
slope, intercept, r_value, _, stderr = linregress(x, y)
y_fit = slope * x + intercept
y_fit_upper = (slope + stderr) * x + intercept
y_fit_lower = (slope - stderr) * x + intercept

# Plot
fig, ax = plt.subplots(figsize=(6, 4), dpi=300)

ax.plot(x, y, 'o', color='black', label='Data')
ax.plot(x, y_fit, '-', color='blue', label=fr'Best fit: $\ln(\mu) = {slope:.2e} \cdot (1/T) + {intercept:.2f}$')
ax.plot(x, y_fit_upper, '--', color='blue', alpha=0.5, label='Upper bound')
ax.plot(x, y_fit_lower, '--', color='blue', alpha=0.5, label='Lower bound')

# Labels and formatting
ax.set_xlabel(r'$1/T$ [1/K]', fontsize=12)
ax.set_ylabel(r'$\ln(\mu)$ [ln(Pa·s)]', fontsize=12)
ax.tick_params(direction='in', which='both', top=True, right=True)
ax.grid(True, linestyle='--', linewidth=0.5)
ax.legend(fontsize=10)

#Display
plt.tight_layout()
plt.show()