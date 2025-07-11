from numpy import array, linspace, max, mean, min, sqrt, std
from tools.statistics.linear_regression import linreg
import matplotlib.pyplot as plt

# 1. Time calibration

T = array([86.417, 86.387, 86.390, 86.381, 86.378])
T_mean = mean(T)
T_uncertainty = sqrt(std(T))

# 2.
length = array([74.6, 75, 75.6, 76, 76.8, 77.7, 78.3])*10**-2
T_heavy_bottom  = array([T_mean, 86.671, 86.966, 87.204, 87.646, 88.226, 88.45])
T_heavy_top     = array([86.737, 84.809, 86.979, 88.685, 87.548, 87.910, 87.99])

# linreg
hb_fun, _, hb_cov = linreg(length, T_heavy_bottom)
ht_fun, _, ht_cov = linreg(length, T_heavy_top)

# plot
x_fit = linspace(min(length)-1, max(length)+1, 1000)
fig, axs = plt.subplots(ncols=1, nrows=1)
axs.plot(x_fit, hb_fun(x_fit))
axs.plot(x_fit, ht_fun(x_fit))

plt.tight_layout()
plt.show()