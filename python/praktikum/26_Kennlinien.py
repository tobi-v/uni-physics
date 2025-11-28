from numpy import array, linspace
from tools.python.checks import CheckLengths

import matplotlib.pyplot as plt

### Schaltung 1 ###

def Ex01():
  V = linspace(2, 40, 20)
  U_tungsten = array([])
  U_carbon = array([])
  I_tungsten = array([])
  I_carbon = array([])
  CheckLengths(V, U_tungsten, U_carbon, I_tungsten, I_carbon)

  fig, axs = plt.subplots(2, 1)

  for ax, U, I, material in zip(axs, [U_tungsten, U_carbon], [I_tungsten, I_carbon], ['Tungsten', 'Carbon']):
    ax.plot(U, I, 'o-', label=f'Kennlinie {material}')
    ax.set_xlabel('Voltage (V)')
    ax.set_ylabel('Current (mA)')
    ax.set_title(f'Kennlinie {material}')
    ax.grid(visible=True)
    ax.legend()

Ex01()