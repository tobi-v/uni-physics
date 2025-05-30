import matplotlib.pyplot as plt
from numpy import append, array, dot, mgrid, pi, transpose, vstack, zeros_like
from numpy.linalg import norm
import numpy as np

from tools.electricity.magnetic_field import BiotSavart, mu_0
from tools.geometry.shapes_1d import CreateLoopXYParallel

### 1. See tools.electricity.magnetic_field -> biot-savart

### 2. Magnetic field for single loop

N       = 10
radius  = 5e-3  # [m]
current = 0.1   # [A]

def BElectricLoop(current, loop: array, pos: array) -> array:    
    loop = append(loop, [loop[0]], axis=0)
    B = 0
    
    for elem, nextElem in zip(loop, loop[1:]):
        dv = nextElem - elem
        delta_r = (elem + nextElem)/2 - pos
        B += BiotSavart(current, dv, delta_r)

    return B

def BElectricLoopMesh(current, loop: array, x, y, z) -> array:    
    pos = array([x, y, z])

    return BElectricLoop(current, loop, pos)
import numpy as np

def BElectricLoop2(I, loop: np.ndarray, pos_grid: np.ndarray) -> np.ndarray:
    """
    Calculate magnetic field B on a 3D grid due to a current loop.

    Parameters:
    - I: current through the loop
    - loop: (N, 3) array of loop vertices
    - pos_grid: (..., 3) array of observation positions (e.g., meshgrid)

    Returns:
    - B: (..., 3) array of magnetic field vectors at each grid point
    """
    loop = np.append(loop, [loop[0]], axis=0)
    B = np.zeros_like(pos_grid)  # same shape as pos_grid, (..., 3)

    for elem, nextElem in zip(loop, loop[1:]):
        dv = nextElem - elem  # (3,)
        r_mid = (elem + nextElem) / 2  # (3,)
        delta_r = r_mid - pos_grid  # (..., 3)
        B += BiotSavart(I, dv, delta_r)  # BiotSavart must support broadcasting

    return B# Define grid pointsimport numpy as np

x2 = np.linspace(-1, 1, 20)
y2 = np.linspace(-1, 1, 20)
z2 = np.linspace(-1, 1, 20)

# Generate meshgrid (3D)
X2, Y2, Z2 = np.meshgrid(x2, y2, z2, indexing='ij')  # shape = (20, 20, 20)

# Stack into single array of shape (20, 20, 20, 3)
pos_grid = np.stack((X2, Y2, Z2), axis=-1)

#B = BElectricLoop(I, loop2, pos_grid)  # B.shape = (20, 20, 20, 3)



#def GetBFromOneLoopList(I, loop: array, positions: array):
#    return array([BElectricLoop(I, loop, pos) for pos in positions])

### 3. Analytic solution for magnetic field inside loop

def BElectricLoopCenter(current, radius):
    return mu_0*current/(2*radius)

r0 = array([0, 0, 0])
loop = CreateLoopXYParallel(radius, 0, N)
numeric_solution = BElectricLoop(current, loop, r0)
analyitc_solution = BElectricLoopCenter(current, radius)
relative_error = abs((numeric_solution[2] - analyitc_solution)/analyitc_solution)

print(f"Numeric value:\t{numeric_solution[2]:.3g}\nAnalytic Value:" \
      "\t{analyitc_solution:.3g}\nRelative error:\t{relative_error*100:.2f} %")

min=-10
max=10
num_elements=50j
X, Y, Z = mgrid[min:max:num_elements, 0:0:1j, min:max:num_elements]*radius
positions = np.stack((X, Y, Z), axis=-1)
#plot_positions = transpose(positions)

#B_field = transpose(GetBFromOneLoopList(I, loop, positions))
B_field = BElectricLoop2(I, loop, positions)

BX = B_field[:, 0, :, 0]
BZ = B_field[:, 0, :, 1]
X2D = X[:, 0, :]
Z2D = Z[:, 0, :]

fig = plt.figure()
ax = fig.add_subplot(3,1,1)
ax.set_title("Numeric B field")
ax.quiver(X2D, Z2D, BX, BZ, width=0.002, scale=1e-6)
plt.show()


### 4.

#def GetBFromPointDPole(M: array, pos: array, exclude_singularities=True, singularity_limit=1e-3) -> array:    
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
#plt.grid()
#
#plt.tight_layout()
#plt.show()
