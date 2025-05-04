import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 10, 10)
y = [2.9, 4.75, 7.3, 9, 11.2, 12.6, 15.1, 17.9, 19.4, 21]

m, b = np.polyfit(x, y, 1)
coeff = np.polyfit(x, y, 1)
linregfun = np.poly1d(coeff)

plt.plot(x,y, 'yo', x, linregfun(x), '--k')
plt.show()