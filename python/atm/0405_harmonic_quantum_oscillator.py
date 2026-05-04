import matplotlib.pyplot as plt
from numpy import abs, exp, linspace, pi, sqrt
from scipy.constants import hbar

def 𝛙(x, t):
    m = 1
    ω = 1
    val = exp(-3j*ω*t/2)
    val = sqrt(2*m*ω/hbar) * val
    val = exp(-1j*ω*t/2) + val
    val = exp(-m*ω*x/(2*hbar)) * val
    val = (m*ω/(hbar*pi))**(1/4) * val
    return val

x = linspace(-1, 1, 1000)

fig, ax = plt.subplots()
ax.plot(x, abs(𝛙(x, 1))**2)

plt.show()