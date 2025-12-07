from numpy import array, inf, linspace
from numpy.typing import NDArray
from scipy.optimize import curve_fit
from tools.python.checks import CheckLengths
from tools.thermo.stefan_boltzmann import StefanBoltzmannRelativeResistance

import matplotlib.pyplot as plt

### Schaltung 1 ###

def Ex01():
  def Power(U: NDArray, I: NDArray) -> NDArray:
    return U*I
  
  def RelativeResistance(R: NDArray, R_0: float) -> NDArray:
    return R/R_0 - 1
  
  def PlotIU(ax: plt.Axes, U:NDArray, I:NDArray, material: str):
    ax.plot(U, I, '+C0', label=f'Current and Voltage of {material}')
    ax.set_xlabel('Voltage (V)')
    ax.set_ylabel('Current (A)')
    ax.set_title(f'Kennlinie {material}')
    ax.grid(visible=True)
    ax.legend()
    plt.tight_layout()

  def PlotPowerRelativeResistance(ax: plt.Axes, R: NDArray, U:NDArray, I:NDArray, material: str):
    ax.plot(RelativeResistance(R, R[0]), Power(U, I), '+C0', label=f'Power and Relative Resistance of {material}')
    ax.set_xlabel('Relative Resistance r')
    ax.set_ylabel('Power (W)')
    ax.set_title(f'Power over Relative Resistance {material}')
    ax.grid(visible=True)
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.legend()
    plt.tight_layout()

  # Messdaten
  V = linspace(2, 40, 20)
  U_tungsten = array([2.05, 3.97, 5.93, 7.96, 9.91, 11.82, 13.78, 15.74, 17.71, 19.65, 21.5, 23.5, 25.4, 27.4, 29.3, 31.3, 33.2, 35.2, 37.1, 39.0])
  I_tungsten = array([3.7, 5.6, 7.1, 8.6, 9.8, 11.0, 12.1, 13.2, 14.2, 15.2, 16.1, 17.0, 17.9, 18.7, 19.5, 20.3, 21.2, 21.9, 22.6, 23.4])*10**-3
  R_tungsten = U_tungsten/I_tungsten
  U_carbon = array([1.9, 4.0, 5.9, 7.8, 9.8, 11.8, 13.7, 15.6, 17.6, 19.5, 21.5, 23.5, 25.4, 27.4, 29.3, 31.2, 33.2, 35.1, 37.1, 39.1])
  I_carbon = array([1.1, 2.1, 3.2, 4.2, 5.4, 6.4, 7.6, 8.7, 9.8, 11.0, 12.2, 13.4, 14.6, 15.8, 17.0, 18.2, 19.5, 20.7, 22.0, 23.3])*10**-3 #A
  R_carbon = U_carbon/I_carbon
  # Pyrometer: 750°C  bei 54.2 V, 28.6 mA
  CheckLengths(V, U_tungsten, U_carbon, I_tungsten, I_carbon)

  # UI-Plots
  fig1, axs = plt.subplots(2, 1)
  for ax, U, I, material in zip(axs, [U_tungsten, U_carbon], [I_tungsten, I_carbon], ['Tungsten', 'Carbon']):
    PlotIU(ax, U, I, material)
  #plt.close(fig1)

  # Power over relative Resistance and comparison to Stefan-Boltzmann Law
  initial_guesses = [[0.001, 0.003, 293], [0.001, -0.003, 293]]
  fig2, axs = plt.subplots(2, 1)
  for ax, R, U, I, material, guess in zip(axs, [R_tungsten, R_carbon], [U_tungsten, U_carbon], [I_tungsten, I_carbon], ['Tungsten', 'Carbon'], initial_guesses):
    PlotPowerRelativeResistance(ax, R, U, I, material)
    popt, _ = curve_fit(StefanBoltzmannRelativeResistance, RelativeResistance(R, R[0]), Power(U, I), p0=guess, bounds=([0, -1, 290], [0.1, 1, 400]))
    area, temp_coeff, T_0 = popt
    print(f"\n--- Params for {material} ---\nArea: {area} m, Temperature Coefficient: {temp_coeff} 1/K, Start temperature: {T_0} K")
  #plt.close(fig2)

def Ex02():
  U1 = array([2.0, 4.0, 4.9, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9])
  I1 = array([0, 0, 0.1, 0.1, 0.2, 0.3, 0.7, 16.5, 56, 125, 161, 500])*10**-3
  U2 = linspace([])
  I2 = array([])*10**-3

Ex01()

plt.show()