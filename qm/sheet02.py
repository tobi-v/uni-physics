import matplotlib.pyplot as plt
from numpy import abs, exp, linspace

### Plot for prob distr.

def DistPlus(x, k, a):
  first = k*exp(-2*k*abs(x+a))
  second = 2*k*exp(-k*abs(x+a)-k*abs(x-a))
  third = k*exp(-2*k*abs(x-a))
  return first + second + third

def DistMinus(x, k, a):
  first = k*exp(-2*k*abs(x+a))
  second = 2*k*exp(-k*abs(x+a)-k*abs(x-a))
  third = k*exp(-2*k*abs(x-a))
  return first - second + third

k = 10
a = 0.5
x = linspace(-10, 10)
yPlus = DistPlus(x, k, a)
yMinus = DistMinus(x, k, a)

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(x, yPlus)
ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(x, yMinus)
plt.show()
