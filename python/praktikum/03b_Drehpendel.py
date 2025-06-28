from numpy import argmax, array, pi
from scipy.signal import find_peaks
from scipy.stats import linregress

### 2.

def daempfung(current, omega, phi):
  slope, _, _, _, _ = linregress(omega, phi)
  beta = -1/slope
  print(f"Dämpfung für {current} mA: beta = {beta}")

def resonance(current, omega, amplitude):
  peaks, _ = find_peaks(omega, amplitude)
  print(f"Peak für Dämpfung von {current} mA at amplitude of omega = {omega[argmax(amplitude)]}")

# Widerstand: 253 mA
current = 251 # [mA]
omega = array([432, 455, 474, 483, 495, 504, 508, 520, 523, 530, 537, 545, 564, 596, 536, 513, 480, 497, 504, 498])/10**3 # [Hz]
ampl = array([649.6, 851.2, 1277, 1770, 2350, 2554, 2352, 1949, 1635, 1344, 1142, 963.2, 649.6, 425.6, 1120, 2083, 1635, 2464, 2554, 2531])/10**3 # [V]
phi = array([14.7, 17.61, 28.5, 41.47, 63.9, 94.2, 115.5, 131.6, 142, 148.1, 152.2, 159.2, 165.3, 172.4, 154.6, 129, 32, 69.4, 96.1, 72.9])*pi/180 # [radian]

print(f"Arraylänge: {omega.size}")

daempfung(current, omega, phi)
resonance(current, omega, ampl)

# Widerstand: 400 mA
omega = array([498, , , , , , , , , , , , , , , , , , , ])/10**3 # [Hz]
ampl = array([, , , , , , , , , , , , , , , , , , , ])/10**3 # [V]
phi = array([, , , , , , , , , , , , , , , , , , , ])*pi/180 # [radian]

#daempfung(current, omega, phi)