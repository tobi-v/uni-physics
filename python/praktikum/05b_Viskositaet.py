import matplotlib.pyplot as plt
from numpy import array, log
from tools.statistics.linear_regression import linreg, plotWithErrorBars

T = array([ 25, 30,   35,   40,   45,   50,   55])+273.15  # [K]
mu = array([50, 42.2, 36.6, 30.2, 25.4, 21.9, 18.8])*1e-3     # [Pa]

arr, _, _ = linreg(1/T, log(mu))

fig, ax = plt.subplots(1, 1)
plotWithErrorBars(ax, 1/T, log(mu), arr)
plt.show()
