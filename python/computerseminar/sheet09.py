from numpy import linalg as npLin,\
    random as npRand,\
    array as npArray,\
    dot as npDot,\
    linspace as npLinspace,\
    meshgrid as npMeshgrid,\
    cos as npCos,\
    pi,\
    sin as npSin
from scipy.optimize import newton as spNewton

# 1

# a

r_start = npArray([0,0])
r_end = npArray([1,.9])

# Bestimmung von phi
def FunOfPhi(phi):
    return (1 - npCos(phi)) / (phi - npSin(phi)) - 0.9

phi_end = spNewton(FunOfPhi, pi)
print(str(phi_end/pi) + " pi")

# Bestimmung von R
R = .9/(1 - npCos(phi_end))
print(R)

#def Cycloid(R, phi):
#    x = R*(phi - npSin(phi))
#    z = R*(1 - npCos(phi))

phi = npLinspace(0, phi_end, 100)



# b
# c

# i
def Line(x):
    return x

# ii
def Ellipsis(x):
    return

# iii
def Root(x):
    return

# 2

c = 1
phi_0 = 0
t1 = 0.2
t2 = 1

x1 = npArray([-3, 0])
x2 = npArray([3, 0])

x = npLinspace(-10, 10, 1000)
y = npLinspace(-10, 10, 1000)
grid = npMeshgrid(x,y)

#def wave(x0, y0, x, y, t):
#    A = 1
#    omega = 2*pi
#    k = omega
#
#    distance = npAbs()
#    amplitude = A
#    return amplitude

# 3

# a

S = npArray([[5, 2, 8], [2, 11, 2], [8, 2, 5]]) * 10
n0 = npArray([2, 2, -1]) / 3

tn0 = npDot(S,n0)
npLin.norm(tn0)

# b

HauptS = npLin.eig(S)
Eigenwerte = HauptS[0]
Eigenvektoren = HauptS[1]

# 4

N = 5000
npRand.seed

x = npRand.rand(N)
y = npRand.rand(N)
