from numpy import array, diag, linspace, ones, sqrt
from numpy.typing import NDArray
from scipy.optimize import curve_fit
from tools.python.checks import CheckLengths
from tools.python.sort import sort_by_x
from tools.statistics.linear_regression import Linreg, ScatterWithErrorBars
from tools.thermo.stefan_boltzmann import StefanBoltzmannRelativeResistance

import matplotlib.pyplot as plt

U_uncertainty = 0.05  # V
I_uncertainty = 0.0001  # A

### Schaltung 1 ###

def Ex01():
  def Power(U: NDArray, I: NDArray) -> NDArray:
    return U*I
  
  def RelativeResistance(R: NDArray, R_0: float) -> NDArray:
    return R/R_0 - 1

  def PlotPowerRelativeResistance(ax: plt.Axes, relative_resistance: NDArray, power:NDArray, material: str):
    ax.plot(relative_resistance, power, '+C0', label=f'Power and Relative Resistance of {material}')
    ax.set_xlabel('Relative Resistance r')
    ax.set_ylabel('Power (W)')
    ax.set_title(f'Power over Relative Resistance {material}')
    ax.grid(visible=True)
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.legend()
    plt.tight_layout()

  def PlotBoltzi(ax: plt.Axes, R: NDArray, U: NDArray, I: NDArray, material: str, guess: list):
    relative_resistance = RelativeResistance(R[1:], R[0])
    power = Power(U[1:], I[1:])
    relative_resistance, power = sort_by_x(relative_resistance, power)

    PlotPowerRelativeResistance(ax, relative_resistance, power, material)
    popt, pcov = curve_fit(StefanBoltzmannRelativeResistance, relative_resistance, power, p0=guess, bounds=([0, -1, 290], [0.1, 1, 400]))
    area, temp_coeff, T_0 = popt
    p_uncertainties = sqrt(diag(pcov))
    area_uncertainty, temp_coeff_uncertainty, T_0_uncertainty = p_uncertainties
    print(f"\n--- Params for {material} ---\n" \
          f"Area:\t\t\t\t{area} +/- {area_uncertainty:.3g} m,\n" \
          f"Temperature Coefficient:\t{temp_coeff} +/- {temp_coeff_uncertainty:.3g} 1/K,\n" \
          f"Start temperature:\t\t{T_0} +/- {T_0_uncertainty:.3g} K")
    ax.plot(relative_resistance, StefanBoltzmannRelativeResistance(relative_resistance, *popt), '--k', label='Fit: Stefan-Boltzmann Law')
    ax.plot(relative_resistance, StefanBoltzmannRelativeResistance(relative_resistance, *(popt + p_uncertainties)), ':r', label='Fit Uncertainty')
    ax.plot(relative_resistance, StefanBoltzmannRelativeResistance(relative_resistance, *(popt - p_uncertainties)), ':r')
    ax.legend()    

  # Messdaten
  V = linspace(2, 40, 20)
  U_tungsten = array([2.05, 3.97, 5.93, 7.96, 9.91, 11.82, 13.78, 15.74, 17.71, 19.65, 21.5, 23.5, 25.4, 27.4, 29.3, 31.3, 33.2, 35.2, 37.1, 39.0])
  I_tungsten = array([3.7, 5.6, 7.1, 8.6, 9.8, 11.0, 12.1, 13.2, 14.2, 15.2, 16.1, 17.0, 17.9, 18.7, 19.5, 20.3, 21.2, 21.9, 22.6, 23.4])*10**-3
  R_tungsten = U_tungsten/I_tungsten
  U_carbon = array([1.9, 4.0, 5.9, 7.8, 9.8, 11.8, 13.7, 15.6, 17.6, 19.5, 21.5, 23.5, 25.4, 27.4, 29.3, 31.2, 33.2, 35.1, 37.1, 39.1])
  I_carbon = array([1.1, 2.1, 3.2, 4.2, 5.4, 6.4, 7.6, 8.7, 9.8, 11.0, 12.2, 13.4, 14.6, 15.8, 17.0, 18.2, 19.5, 20.7, 22.0, 23.3])*10**-3 #A
  R_carbon = U_carbon/I_carbon  
  U_carbon_filtered = array([1.9, 4.0, 7.8, 9.8, 13.7, 15.6, 19.5, 21.5, 23.5, 25.4, 27.4, 29.3, 31.2, 33.2, 35.1, 37.1, 39.1])
  I_carbon_filtered = array([1.1, 2.1, 4.2, 5.4, 7.6, 8.7, 11.0, 12.2, 13.4, 14.6, 15.8, 17.0, 18.2, 19.5, 20.7, 22.0, 23.3])*10**-3 #A
  R_carbon_filtered = U_carbon_filtered/I_carbon_filtered
  # Pyrometer: 750°C  bei 54.2 V, 28.6 mA
  CheckLengths(V, U_tungsten, U_carbon, I_tungsten, I_carbon)
  CheckLengths(U_carbon_filtered, I_carbon_filtered, R_carbon_filtered)

  # UI-Plots
  fig1, axs = plt.subplots(2, 1)
  for ax, U, I, material in zip(axs, [U_tungsten, U_carbon], [I_tungsten, I_carbon], ['Tungsten', 'Carbon']):
    ScatterWithErrorBars(ax, U, I, x_absErr=U_uncertainty, y_absErr=I_uncertainty, scatter_label="Measured Values", xlabel="Voltage (V)", ylabel="Current (A)", title=f'Voltage and Current for {material}')
    plt.tight_layout()
  plt.close(fig1)

  # Power over relative Resistance and comparison to Stefan-Boltzmann Law
  initial_guesses = [[0.001, 0.003, 293], [0.001, -0.003, 293]]
  fig2, axs = plt.subplots(2, 1)
  for ax, R, U, I, material, guess in zip(axs, [R_tungsten, R_carbon], [U_tungsten, U_carbon], [I_tungsten, I_carbon], ['Tungsten', 'Carbon'], initial_guesses):
    PlotBoltzi(ax, R, U, I, material, guess)
  plt.close(fig2)
  fig3, ax = plt.subplots()
  PlotBoltzi(ax, R_carbon_filtered, U_carbon_filtered, I_carbon_filtered, 'Filtered Carbon Data', initial_guesses[1])
  plt.close(fig3)

def Ex02():
  U_through = array([2.0, 4.0, 4.9, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9])
  I_through = array([0, 0, 0.1, 0.1, 0.2, 0.3, 0.7, 16.5, 56, 125, 161, 500])*10**-3
  U_block = array([.1, .2, .4, .5, .7, .8, .9, 1.])
  I_block = array([0, 0, 0, .1, 11, 44, 75., 120])*10**-3
  CheckLengths(U_through, I_through); CheckLengths(U_block, I_block)

  def PowerLossHyperbola(U: NDArray, P_max: float) -> NDArray:
    return (P_max/U)

  # UI-Plots and power loss hyperbola
  P_max = .25 # W
  fig1, axs1 = plt.subplots(2, 1)
  for ax, U, I, direction in zip(axs1, [U_through, U_block], [I_through, I_block], ['Forward Direction', 'Reverse Direction']):
    U_plot = linspace(0, max(U)*1.1, 100)
    ax.plot(U_plot, PowerLossHyperbola(U_plot, P_max), '--r', label=r'Power Loss Hyperbola for $P_\mathrm{max} = %.2f W$' % P_max)
    ax.plot(U_plot, 0.1*ones(len(U_plot)), '--k', label=r'$I_\mathrm{max} = 100 mA$')
    ScatterWithErrorBars(ax, U, I, x_absErr=U_uncertainty, y_absErr=I_uncertainty, scatter_label="Measured Values", xlabel="Voltage (V)", ylabel="Current (A)", title=f'Voltage and Current for {direction}')
    ax.set_ylim(0, max(max(I)*1.1, 0.5))
    plt.tight_layout()
  plt.close(fig1)

  # half logarithmich UI-plots
  fig2, axs2 = plt.subplots(2, 1)
  for ax, U, I, direction in zip(axs2, [U_through, U_block], [I_through, I_block], ['Forward Direction', 'Reverse Direction']):
    ScatterWithErrorBars(ax, U, I, x_absErr=U_uncertainty, y_absErr=I_uncertainty, scatter_label="Measured Values", xlabel="Voltage (V)", ylabel="Current (A)", title=f'Voltage and Current for {direction} (half-log scale)')
  ax.set_yscale('log')
  plt.tight_layout()
  plt.close(fig2)

def Ex03():
  R_V = 330  # Ohm
  U_e = linspace(1, 20, 20)
  U_a = array([1.0, 1.9, 3.0, 3.9, 4.9, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4])
  CheckLengths(U_e, U_a)

  U_e_smooth = U_e[4:]
  U_a_smooth = U_a[4:]
  stabilized_in_out_fun, coeff, cov = Linreg(U_e_smooth, U_a_smooth)
  slope = coeff[0]
  slope_uncertainty = sqrt(cov[0][0])
  y_intercept = coeff[1]
  y_intercept_uncertainty = sqrt(cov[1][1])

  fig, ax = plt.subplots()
  ax.plot(U_e_smooth, stabilized_in_out_fun(U_e_smooth), '--r', label=f'Linear Fit: $U_\\mathrm{{a}} = {coeff[0]:.3f} U_\\mathrm{{e}} + {coeff[1]:.3f}$')
  ax.plot(U_e_smooth, (slope + slope_uncertainty)*U_e_smooth + (y_intercept + y_intercept_uncertainty), ':r', label='Fit Uncertainty')
  ax.plot(U_e_smooth, (slope - slope_uncertainty)*U_e_smooth + (y_intercept - y_intercept_uncertainty), ':r')
  ScatterWithErrorBars(ax, U_e, U_a, x_absErr=U_uncertainty, y_absErr=I_uncertainty, scatter_label="Measured Values", xlabel=r"Input Voltage $U_\mathrm{e} (V)$", ylabel=r"Output Voltage $U_\mathrm{a} (V)$", title=f"In- and Output Voltage for Voltage Stabilization")
  plt.tight_layout()
  plt.close(fig)

  print(f"\nStabilization factor G = {1/slope:.2f} +/- {slope_uncertainty/slope**2:.2f}")

def Ex04():
  I_BE = array([20, 40])*10**-6
  U_CE = linspace(4, 40, 10)
  I_CE_20 = array([6.5, 6.7, 6.9, 7.3, 7.5, 7.8, 8.1, 8.5, 8.8, 9.2  ])*10**-3
  I_CE_40 = array([15.0, 16.1, 17.1, 18.5, 19.1, 20.0, 20.8, 21.5, 22.0, 22.2])*10**-3
  CheckLengths(U_CE, I_CE_20, I_CE_40)






#Ex01()
#Ex02()
#Ex03()
Ex04()

plt.show()