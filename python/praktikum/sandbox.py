import numpy as np
import matplotlib.pyplot as plt

p11 = np.array([3, 5, 7])
p12 = np.array([3, 5, 7])
p13 = np.array([3, 5, 7])
p21 = np.array([[3, 5, 7],
              [4, 6, 8],
              [5, 7, 9]])
p22 = np.array([[3, 5, 7],
              [4, 6, 8],
              [5, 7, 9]])
p23 = np.array([[3, 5, 7],
              [4, 6, 8],
              [5, 7, 9]])

point0 = [2, 4, 6]
print(f"point0: {point0}")
point1 = [p11, p12, p13]
print(f"point1: {point1}")
point2 = [p21, p22, p23]
print(f"point2: {point2}")

args0 = point0[:]
print(f"args0: {args0}")
args1 = [p.tolist() for p in point1]
print(f"args1: {args1}")
args2 = [p.tolist() for p in point2]
print(f"args2: {args2}")

#x = np.linspace(1, 10, 10)
#y = [2.9, 4.75, 7.3, 9, 11.2, 12.6, 15.1, 17.9, 19.4, 21]
#
#m, b = np.polyfit(x, y, 1)
#coeff = np.polyfit(x, y, 1)
#linregfun = np.poly1d(coeff)
#
#plt.plot(x,y, 'yo', x, linregfun(x), '--k')
#plt.show()