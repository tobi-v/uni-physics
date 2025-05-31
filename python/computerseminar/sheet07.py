import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as npl
#from scipy.fft import fft, fftfreq
#from scipy.linalg import eigh

# 1 Stratosphere

height_start = 38969
c_w = 1.1
area_felix = 0.4
g = 9.81

#def friction(rho, v):
#    return c_w*rho*A_felix*v**2/2

def rho(height):
    rho_0 = 1.24
    p_0 = 101300

    return rho_0 * np.exp2(-rho_0*g*height/p_0)

# a


# 2 Pendulum

l = 5
phi_0 = 0
dphi_0 = 1

#def dgl_exact(t, y):
#    phi, dphi = y
#    return [dphi, -(g/l)*np.sin(phi)]

#solution_exact =
#t_exact = solution_exact.t
#phi_exact = solution_exact.y

# c

#def dgl_approx(t, y):
#    phi, dphi = y
#    return [dphi, -(g/l)*phi]

# 3 Coupled feathers

m1 = 1
m2 = 1
k_a = 1
k_i = 20
x1_0 = 0.1
x2_0 = 0.2

times = []

# a

def sim(dt, t_max):
    t = 0
    x1_vals = []
    x2_vals = []
#    v1_vals = []
#    v2_vals = []
    while t < t_max:
#        F1 =
#        F2 =
#
#        a1 =
#
#        v1 =
#
#        x1 =

        t += dt

        times.append(t)
#        x1_vals.append(x1)
#        v1_vals.append(v1)

    return x1_vals, x2_vals

plt.figure()

plt.tight_layout()
plt.show()

# b

#np.max(x1_vals)
#np.max(x2_vals)

# d

A = np.array([[(k_a + k_i)/m1, -k_i/m1], [-k_i/m1, (k_a+k_i)/m2]])
print(A)
EW, EV = npl.eig(A)
EF = np.sqrt(EW)/(2*np.pi)
print('Eigenfrequenzen f_i in Hz: ', EF)

# Extra

#t = np.arange(0, T, dt)

#coefficients = smth1 @ smth2

# 4

# a

#def dif(t, x):
#    h, v = x
#
#    a_g = (g*m_rocket) / h**2
#    dvdt = a_schub - a_g
#    return [v, dvdt]
#
#sol = solve_ivp(dif, ...)

# c

#nullstellen = np.where(np.diff(np.sign(h1)) != 0)[0]
#t_max = t1[nullstellen[1]]
#
#h_max = np.max(h1)
#
#v_max = np.max(v1)
#
#hv1 = np.argmax(v1)
#
#v_ende = v1[h1<=0][1]