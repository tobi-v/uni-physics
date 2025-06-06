from matplotlib import pyplot as plt
from numpy import linspace

from tools.electricity.magnetic_field import HelmholtzAlongZ

current = 10    # [A]
turns   = 100
radius  = 10e-2  # [m]

distances = [radius/2, radius, 2*radius]

z = linspace(-25e-2, 25e-2, 1000)

def plot_helmholtz(ax, dist: float):
    B = HelmholtzAlongZ(z, current, radius, dist, turns)
    print(f"\nDistance: {dist} \t"
          f"B(0) = {HelmholtzAlongZ(0, current, radius, dist, turns)}")
    ax.plot(z, B)
    ax.grid()
    ax.set_title(f"Distance: {dist}")

fig, axs = plt.subplots(nrows=3, ncols=1)

for ii, distance in enumerate(distances):
    plot_helmholtz(axs[ii], distance)

plt.tight_layout()
plt.grid()
plt.grid()
plt.show()
