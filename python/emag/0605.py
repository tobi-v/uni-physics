from numpy import append, array

from tools.electricity.magnetic_field import BiotSavart
from tools.geometry.shapes_1d import CreateLoopXYParallel

### 1. See tools.electricity.magnetic_field -> biot-savart

### 2. B field for single loop

N       = 10
radius  = 5e-3  # [m]
I       = 0.1   # [A]

loop = CreateLoopXYParallel(radius, 0, N)


def GetBFromOneLoop(I, loop: array, pos: array) -> array:    
    loop = append(loop, [loop[0]], axis=0)
    B = 0
    
    for elem, nextElem in zip(loop, loop[1:]):
        dv = nextElem - elem
        delta_r = (elem + nextElem)/2 - pos
        B += BiotSavart(I, dv, delta_r)

    return B

def GetBFromOneLoopList(I, loop: array, positions: array):
    return array([GetBFromOneLoop(I, loop, pos) for pos in positions])