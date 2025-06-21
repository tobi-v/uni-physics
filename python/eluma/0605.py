from matplotlib import cm, pyplot
from numpy import array, log10, mgrid, stack, sqrt, zeros_like
from numpy.linalg import norm

from tools.electricity.magnetic_field import BOfLoopCenter, BOfLoopNumeric,\
      BOfPointDipole, MagneticMomentZ
from tools.geometry.shapes_1d import CreateLoopXYParallel

fig, axs = pyplot.subplots(figsize=(15,10), nrows=3, ncols=2)

### 1. See tools.electricity.magnetic_field -> biot-savart

### 2. See tools.electricity.magnetic_field -> BOfLoopNumeric

### 3.1 Compare analytic and numeric solution at loop center

loop_points = 100
radius      = 5e-3  # [m]
current     = 0.1   # [A]

r0 = array([0.0, 0.0, 0.0])
loop = CreateLoopXYParallel(radius, loop_points)
B_numeric = BOfLoopNumeric(current, loop, r0)
B_analytic = BOfLoopCenter(current, radius)
relative_error = abs((B_numeric[2] - B_analytic)/B_analytic)

print(f"Numeric value:\t{B_numeric[2]:.3g}\nAnalytic Value:" \
      f"\t{B_analytic:.3g}\nRelative error:\t{relative_error*100:.2f} %")

### 3.2 Magnetic Field Lines

min = -100*radius
max = 100*radius
sample_positions = 100
Z, X = mgrid[min:max:sample_positions*1j, min:max:sample_positions*1j]
Y = zeros_like(X)
positions = stack((X, Y, Z), axis=-1)

B_numeric = BOfLoopNumeric(current, loop, positions)
BX = B_numeric[:, :, 0]
BZ = B_numeric[:, :, 2]

axs[0][0].set_title("Numeric B field")
magnitude = norm(B_numeric, axis=-1)
axs[0][0].streamplot(X, Z, BX, BZ, density=1.5, color=log10(magnitude), cmap='plasma')

### 4. Comparison of numeric biot-savart and point-dipole model

mag_mom = MagneticMomentZ(radius, current)
B_dipole = BOfPointDipole(mag_mom, positions)
B_dipoleX = B_dipole[:, :, 0]
B_dipoleZ = B_dipole[:, :, 2]

axs[1][0].set_title("B field of magnetic dipole")
magnitude = norm(B_dipole, axis=-1)
axs[1][0].streamplot(X, Z, B_dipoleX, B_dipoleZ, density=1.5, color=log10(magnitude),
                  cmap='plasma')

error = norm(B_numeric - B_dipole, axis=-1) / norm(B_numeric, axis=-1)
logarithmic_error = log10(error)
heatmap = axs[0][1].pcolormesh(X, Z, logarithmic_error, shading='auto', cmap='plasma')
axs[0][1].set_title("Log-Relative Error Heatmap")
fig.colorbar(heatmap, label="log(|B_num - B_ref| / |B_num|)")

axs[1][1].set_title(r'$r_{1\%}$')
contour = axs[1][1].contour(X, Z, error, levels=[0.01], colors='white', linewidths=2)
axs[1][1].clabel(contour, fmt={0.01: '1% Error'}, fontsize=10)
im = axs[1][1].pcolormesh(X, Z, log10(error), shading='auto', cmap=cm.viridis)
fig.colorbar(im, ax=axs[1][1], label=r'$\log_{10}(\epsilon)$')
axs[1][1].set_title(r'$\epsilon = 1\%$ Contour')
axs[1][1].set_xlabel("x [m]")
axs[1][1].set_ylabel("z [m]")

R = sqrt(X**2 + Z**2)
mask = error < 0.01
if mask.any():
    r_1_percent = R[mask].min()
    print(f"All points inside of r = {r_1_percent/radius:.2f} * Rc have a relative error of more than 1%.")
else:
    print("All points have relative error > 1%.")

# 5. Coil    

pyplot.grid()
pyplot.tight_layout()
pyplot.show()
