from matplotlib import pyplot as plt
from numpy import exp, linspace, pi, sqrt, zeros_like
from scipy.integrate import quad

# Placeholder constants
mass = 1
omega = 1
hbar = 1

def probability_density(u):
    return (mass * omega / (pi * hbar)) ** (1/2) * exp(-mass * omega * u ** 2 / hbar)

x0 = sqrt(hbar / (2 * mass * omega))
u_range = linspace(-10 * x0, 10 * x0, 100)
P_u_numerical = zeros_like(u_range)

# Calculate P(u) using numerical integration for each u
for i, u in enumerate(u_range):
    integral, _ = quad(probability_density, u - x0/2, u + x0/2)
    P_u_numerical[i] = integral

plt.figure(figsize=(10, 6))
plt.plot(u_range, P_u_numerical, color='blue')
plt.title(r'Probability $P(u)$ for $u \in (-10x_0, 10x_0)$')
plt.xlabel(r'$u$')
plt.ylabel(r'$P(u)$')
plt.grid(True)
plt.show()