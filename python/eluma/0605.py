import matplotlib.pyplot as plt
from numpy import array, log, mgrid, stack, zeros_like
from numpy.linalg import norm

from tools.electricity.magnetic_field import BOfLoopCenter, BOfLoopNumeric
from tools.geometry.shapes_1d import CreateLoopXYParallel

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

B_field = BOfLoopNumeric(current, loop, positions)
BX = B_field[:, :, 0]
BZ = B_field[:, :, 2]

fig, axs = plt.subplots(figsize=(3,9), nrows=3, ncols=1)
axs[0].set_title("Numeric B field")
magnitude = norm(B_field, axis=-1)
axs[0].streamplot(X, Z, BX, BZ, density=1.5, color=log(magnitude), cmap='plasma')


### 4.

#def GetBFromPointDPole(M: array,
#                       pos: array,
#                       exclude_singularities=True,
#                       singularity_limit=1e-3) -> array:    
#    distance = norm(pos)
#    if(exclude_singularities and (distance < singularity_limit)):
#        distance = distance + 1e-3#return array([0, 0, 0])
#    return mu_0*(3*dot(M, pos)*pos - M*distance**2)/(4*pi*distance**5)
#
#def GetBFromPointDPoleList(M:array, positions: array) -> array:
#    return array([GetBFromPointDPole(M, pos) for pos in positions])
#
#M_loop = array([0, 0, pi*(radius**2)*I])
#B_dipole = transpose(GetBFromPointDPoleList(M_loop, positions))
#
#ax = fig.add_subplot(3,1,2)
#ax.set_title("B from dipole")
#ax.quiver(plot_positions[0], plot_positions[2], B_dipole[0], B_dipole[2], width=0.002)
#plt.grid()
#
#B_diff_arr = array([norm(elem) for elem in (transpose(B_field) - transpose(B_dipole))])
#B_field_norm = array([norm(elem) for elem in transpose(B_field)])
#
#print(B_diff_arr)
#B_error = B_diff_arr/B_field_norm
#ax = fig.add_subplot(3,1,3)
#ax.set_title("B from dipole")
#ax.contour(plot_positions[0], plot_positions[2], B_error)
plt.grid()
plt.tight_layout()
plt.show()
