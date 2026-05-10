from numpy import abs, exp, linspace, pi, sqrt
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

m = 1.0
ω = 1.0
hbar = 1.0

x = linspace(-5, 5, 1000)

def 𝛙_0(x):
    return (m*ω / (pi*hbar))**(1/4) * exp(-m*ω*x**2 / (2*hbar))

def 𝛙_1(x):
    return (m*ω / (pi*hbar))**(1/4) * sqrt(2*m*ω / hbar)*x * exp(-m*ω*x**2 / (2*hbar))

def 𝛙(x, t):
    return 𝛙_0(x)*exp(-1j*ω / 2*t) + 𝛙_1(x)*exp(-1j*3*ω / 2*t)

def prob_density(x, t):
    return abs(𝛙(x, t))**2

fig, ax = plt.subplots()
ax.set_xlabel('Position x')
ax.set_ylabel('$|\\psi(x,t)|^2$')
ax.set_title('Zeitliche Veränderung der Wahrscheinlichkeitsdichte')

line, = ax.plot(x, prob_density(x, 0), lw=2)

def update(t):
    line.set_ydata(prob_density(x, t))
    ax.set_title(f'Zeitliche Veränderung der Wahrscheinlichkeitsdichte (t = {t:.2f})')
    return line,

ani = FuncAnimation(fig, update, frames=linspace(0, 2*pi/ω, 100), interval=50, blit=True)

plt.grid(True)
plt.show()