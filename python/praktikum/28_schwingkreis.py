from numpy import array, diff, log, mean, std
from numpy.typing import NDArray
from tools.statistics.linear_regression import plotWithErrorBars
from tools.python.checks import CheckLengths
from tools.python.plot import DefaultScatter

import matplotlib.pyplot as plt

t_uncertainty = 10**-6 # s
U_uncertainty = 0.2*10**-3 # V

### Teil 1 freie Schwingung
t = array([0, 90, 190, 280, 380, 470, 570, 660, 750, 850, 940, 1040, 1130, 1230, 1320, 1410, 1510, 1600, 1700, 1790, 1880, 1980, 2070])*10**-6
U = array([63.2, 59.2, 54.4, 51.2, 48, 43.2, 40, 38.4, 35.2, 34.4, 30.4, 28.8, 28, 25.6, 23.2, 21.6, 20.8, 20, 16.8, 16, 16, 14.4, 12.8])*10**-3
CheckLengths(t, U)

def OpenLoopDamping(t: NDArray, U: NDArray):
  """Berechnet das logarithmische Dekrement und die Dämpfungskonstante eines offenen Schwingkreises.

  Args:
    t (array): Zeitpunkte der Messungen in Sekunden.
    U (array): Amplituden in Volt.

  Returns:
    damping (float): Dämpfungskonstante.
    damping_uncertainty (float): Unsicherheit der Dämpfungskonstante.
  """
  delta = log(U[:-1] / U[1:])

  T = diff(t)
  decrements = delta / T

  damping = mean(decrements)/2
  damping_uncertainty = std(decrements)/2

  return damping, damping_uncertainty

damping, damping_uncertainty = OpenLoopDamping(t, U)
print("Dämpfungskonstante:", damping, "±", damping_uncertainty, "1/s")

_, ax =  plt.subplots(1, 1)
DefaultScatter(ax, t, U, xlabel="Zeit (s)", ylabel="Spannung (V)", title="Freie Schwingung: Spannung über Zeit")
plt.tight_layout()
plt.show()

### Teil 2: Erzwungene Schwingung 
omega = array([10, 15, 20, 30, 50, 70, 125, 250, 500,
  700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700,
               2500, 4000, 5500, 7500, 10000, 15000, 20000, 25000, 30000])
U_chain = array([3000, 3000, 2960, 2940, 2880, 2760, 2520, 2100, 1920,
  1440, 1420, 1420, 1420, 1400, 1400, 1400, 1400, 1400, 1400, 1400,
                 1440, 1500, 1600, 1720, 1860, 2080, 2140, 2800, 2820])*10**-3
U_R = array([96, 146, 184, 272, 420, 552, 792, 1040, 1170,
  944, 944, 952, 952, 952, 952, 952, 952, 952, 952, 952,
             944, 896, 840, 744, 616, 360, 192, 320, 528])*10**-3
phi = array([90, 86, 85, 78, 72, 70, 60, 40, 20,
  16.5, 13, 9, 6, 6, 4.5, 3, 1.5, 0, -1, -3,
             -12, - 20, -28, -35, -40, -38, 6, 56, 77]) # degree
CheckLengths(omega, U_chain, U_R, phi)

### 3.

U_source = 4
omega = array([10, 100, 1000, 5000, 6000, 6500, 7000, 7250, 7500, 7750, 8000, 8250, 8500, 8750, 9000, 9250, 9500, 9750, 10000, 10500, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 25000, 30000, 40000, 60000, 80000, 99990])
U_signal = array([3.36, 3.36, 3.36, 2.76, 2.56, 2.48, 2.4, 2.32, 2.32, 2.32, 2.24, 2.24, 2.16, 2.12, 2.08, 2.08, 2, 1.96, 1.92, 1.88, 1.8, 1.68, 1.6, 1.52, 1.44, 1.36, 1.28, 1.2, 1.16, 1.12, 0.92, 0.92, 0.72, 0.52, 0.44, 0.36])
phi = array([0, 1, -6, -33, -41, -42, -42, -44, -46, -46, -48, -49, -50, -50, -50, -52, -50, -51, -52, -54, -53, -60, -60, -60, -65, -65, -62, -67, -64, -70, -80, -66, -85, -60, -87, -90]) # degree
CheckLengths(omega, U_signal, phi)