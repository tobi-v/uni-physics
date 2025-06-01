import matplotlib.pyplot as plt
import numpy as np
#from scipy.integrate import quad

# A1

class HeavyBody():

    def __init__(self, mass, radius, pos, vel):
        self.mass = mass
        self.radius = radius
        self.pos = pos
        self.vel = vel

balls = [HeavyBody(mass=1, radius=0.2, pos=np.array([0,0]), vel=np.array([1,1])),
         HeavyBody(mass=2, radius=0.2, pos=np.array([4, 0]), vel=np.array([-1, 1]))]

M = balls[0].mass+balls[1].mass
xd = balls[0].pos - balls[1].pos
vd = balls[0].vel - balls[1].vel

# a

# Could be replaced to a for loop over 2 idx in order to expand to n bodies
balls[0].vel = balls[0].vel - 2*balls[1].mass/M * np.dot(vd, xd)/np.dot(xd, xd) * xd
balls[1].vel = balls[1].vel - 2*balls[0].mass/M * np.dot(vd, xd)/np.dot(xd, xd) * xd

#np.angle(balls[0].vel, balls[1].vel)

# b

# c

# 2

# a

G = 6.6743e-11
r0 = np.array([])
v0 = np.array([])
M = 0
m = 0

dt = 100
t1 = 10e6

t = 0

while t < t1:

    #r_magnitude = np.linalg.norm(r)
    F_gravity = 0 # insert formula

    t += dt

# 3

# a

def vel(r, eta, dp, R, L):
    return -(dp / (4 * eta * L)) * (R**2 - r**2)

# b
# c

# 4

center = (0,0)
R = 5

# a

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

circle = plt.Circle(center, R)
plot = ax.plot([], [])
ax.add_patch(circle)
plt.show()

# b

pos = np.array([0,0])
while(np.norm(pos) < 5):
    x = 1

# c

# Ergebnis ca 5,74m in 1s

# d

# Ergebnis 5m in 1s