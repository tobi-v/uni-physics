from numpy import array, linspace
from tools.python.checks import CheckLengths

import matplotlib.pyplot as plt

### Schaltung 1 ###

def Ex01():
  V = linspace(2, 40, 20)
  U_tungsten = array([2.05, 3.97, 5.93, 7.96, 9.91, 11.82, 13.78, 15.74, 17.71, 19.65, 21.5, 23.5, 25.4, 27.4, 29.3, 31.3, 33.2, 35.2, 37.1, 39.0])
  I_tungsten = array([3.7, 5.6, 7.1, 8.6, 9.8, 11.0, 12.1, 13.2, 14.2, 15.2, 16.1, 17.0, 17.9, 18.7, 19.5, 20.3, 21.2, 21.9, 22.6, 23.4]) *10**-3
  U_carbon = array([1.9, 4.0, 5.9, 7.8, 9.8, 11.8, 13.7, 15.6, 17.6, 19.5, 21.5, 23.5, 25.4, 27.4, 29.3, 31.2, 33.2, 35.1, 37.1, 39.1])
  I_carbon = array([1.1, 2.1, 3.2, 4.2, 5.4, 6.4, 7.6, 8.7, 9.8, 11.0, 12.2, 13.4, 14.6, 15.8, 17.0, 18.2, 19.5, 20.7, 22.0, 23.3])*10**-3 #A
  # Pyrometer: 750°C  bei 54.2 V, 28.6 mA
  CheckLengths(V, U_tungsten, U_carbon, I_tungsten, I_carbon)

  fig, axs = plt.subplots(2, 1)

  for ax, U, I, material in zip(axs, [U_tungsten, U_carbon], [I_tungsten, I_carbon], ['Tungsten', 'Carbon']):
    ax.plot(U, I, 'o-', label=f'Kennlinie {material}')
    ax.set_xlabel('Voltage (V)')
    ax.set_ylabel('Current (mA)')
    ax.set_title(f'Kennlinie {material}')
    ax.grid(visible=True)
    ax.legend()

def Ex02():
  U1 = array([2.0, 4.0, 4.9, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9])
  I1 = array([0, 0, 0.1, 0.1, 0.2, 0.3, 0.7, 16.5, 56, 125, 161, 500])*10**-3
  U2 = linspace([])
  I2 = array([])*10**-3

Ex01()