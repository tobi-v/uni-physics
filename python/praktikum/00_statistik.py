import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

MEAN = 0
SIGMA = 1
N = 1000
M = 1

def mean(distr):
    return np.mean(distr, axis=0)

def std(distr):
    return np.std(distr, axis=0, ddof=1)

def kurtosis(distr):
    return sp.stats.kurtosis(distr, axis=0, fisher=True)

def gauss_dist(x, mean, sigma):
    return 1/(np.sqrt(2*np.pi) * sigma) * np.exp(-0.5*((x-mean)/sigma)**2)

#def wurf(p, x_0, theta):
#    g = 9.81
#    m = 1
#    v = p/m
#    v_y = v*np.sin(theta)
#    v_x = v*np.cos(theta)
#    t_E = (v_y + np.sqrt(v_y**2 + 2*g*y_0)) / g
#    x_E = ...


np.random.seed(13)
uniform_distr = np.random.uniform(-1, 1, (N, M))

#plt.yscale('log')

# Punkt 1
#N = 1000
#M = 1
#normal_distr = np.random.normal(MEAN, SIGMA, (N, M))
#x = np.linspace(-4, 4)
#mean = mean(normal_distr)
#plt.hist(normal_distr, bins=100, density=True)
#plt.plot(x, gauss_dist(x, 0, 1))
#plt.show()

# Punkt 2
N = 1000
M = 5
normal_distr = np.random.uniform(-1,1,(N,M))
a = np.linspace(1,N,N)
cum_sum = np.cumsum(normal_distr, axis=0)
cum_mean1 = cum_sum[:,0] / a
cum_mean2 = cum_sum[:,1] / a
cum_mean3 = cum_sum[:,2] / a
cum_mean4 = cum_sum[:,3] / a
cum_mean5 = cum_sum[:,4] / a

Y = [SIGMA / np.sqrt(i-1) for i in range(2, N+1)]
Y.insert(0, SIGMA)
Y = np.transpose(Y)

plt.subplot(3,2,1)
plt.plot(cum_mean1, 'b')
plt.plot(cum_mean2, 'b')
plt.plot(cum_mean3, 'b')
plt.plot(cum_mean4, 'b')
plt.plot(cum_mean5, 'b')
plt.plot(Y, 'r')
plt.plot(-Y, 'r')
plt.xscale('log')

def cum_std(vec):
    res = []
    for i in range(1,N):
        res.append(np.std(vec[1:i]))
    return res

cumstd1 = cum_std(normal_distr[:,0])
cumstd2 = cum_std(normal_distr[:,1])
cumstd3 = cum_std(normal_distr[:,2])
cumstd4 = cum_std(normal_distr[:,3])
cumstd5 = cum_std(normal_distr[:,4])

Y = [SIGMA / np.sqrt(i-1) for i in range(2, N+1)]
Y.insert(0, SIGMA)
Y = np.transpose(Y)

plt.subplot(3,2,2)
plt.plot(cumstd1, 'b')
plt.plot(cumstd2, 'b')
plt.plot(cumstd3, 'b')
plt.plot(cumstd4, 'b')
plt.plot(cumstd5, 'b')
plt.plot(1+Y, 'r')
plt.plot(1-Y, 'r')
plt.xscale('log')

def cum_kurt(vec):
    res = []
    for i in range(1,N):
        res.append(np.abs(kurtosis(vec[1:i]))**(1/4))
    return res

cumstd1 = cum_kurt(normal_distr[:,0])
cumstd2 = cum_kurt(normal_distr[:,1])
cumstd3 = cum_kurt(normal_distr[:,2])
cumstd4 = cum_kurt(normal_distr[:,3])
cumstd5 = cum_kurt(normal_distr[:,4])

Y = [SIGMA / np.sqrt(i-1) for i in range(2, N+1)]
Y.insert(0, SIGMA)
Y = np.transpose(Y)

plt.subplot(3,2,3)
plt.plot(cumstd1, 'b')
plt.plot(cumstd2, 'b')
plt.plot(cumstd3, 'b')
plt.plot(cumstd4, 'b')
plt.plot(cumstd5, 'b')
plt.plot(2**(1/4)*Y, 'r')
plt.plot(-2**(1/4)*Y, 'r')
plt.xscale('log')
plt.yscale('log')
plt.show()