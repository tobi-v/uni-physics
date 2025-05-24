import matplotlib.pyplot as plt
from numpy import append, array, linspace, log, mgrid, ravel, transpose, vstack, zeros_like

from tools.electricity.magnetic_field import BiotSavart, mu_0
from tools.geometry.shapes_1d import CreateLoopXYParallel

### 1. See tools.electricity.magnetic_field -> biot-savart

### 2. Magnetic field for single loop

N       = 10
radius  = 5e-3  # [m]
I       = 0.1   # [A]

def BElectricLoop(I, loop: array, pos: array) -> array:    
    loop = append(loop, [loop[0]], axis=0)
    B = 0
    
    for elem, nextElem in zip(loop, loop[1:]):
        dv = nextElem - elem
        delta_r = (elem + nextElem)/2 - pos
        B += BiotSavart(I, dv, delta_r)

    return B

def GetBFromOneLoopList(I, loop: array, positions: array):
    return array([BElectricLoop(I, loop, pos) for pos in positions])

### 3. Analytic solution for magnetic field inside loop

def BElectricLoopCenter(I, radius):
    return mu_0*I/(2*radius)

r0 = array([0, 0, 0])
loop = CreateLoopXYParallel(radius, 0, N)
numeric_solution = BElectricLoop(I, loop, r0)
analyitc_solution = BElectricLoopCenter(I, radius)
relative_error = abs((numeric_solution[2] - analyitc_solution)/analyitc_solution)

print(f"Numeric value:\t{numeric_solution[2]:.3g}\nAnalytic Value:\t{analyitc_solution:.3g}\nRelative error:\t{relative_error*100:.2f} %")

# Create meshgrid from [-10, 0, -10]/Rc to [10, 0, 10]/Rc
min=-2
max=2
num_elements=50j
X, Y, Z = mgrid[min:max:num_elements, 0:0:1j, min:max:num_elements]*radius
positions = transpose(vstack([X.ravel(), zeros_like(X.ravel()), Z.ravel()]))
plot_positions = transpose(positions)

B_field = transpose(GetBFromOneLoopList(I, loop, positions))

fig = plt.figure()
ax = fig.add_subplot()
ax.quiver(plot_positions[0], plot_positions[2], B_field[0], B_field[2], width=0.002)
plt.grid()
plt.show()
