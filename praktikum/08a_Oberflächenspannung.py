import numpy as np
import matplotlib.pyplot as plt

def FehlerFortpflanzung(F_mean, delF):
    R_mean = 32*10**(-3)
    delR = np.sqrt(0.5)*10**-3
    F_component = 1 / (2*np.pi*R_mean)
    r_component = F_mean / (2*np.pi*R_mean**2)
    return np.sqrt((F_component*delF)**2 + (r_component*delR)**2)

D_RingA = 65.0*10**(-3)
D_RingI = 63.0*10**(-3)
r_Ring_mean = (D_RingA + D_RingI) / 4.0
r_Ring_std = np.sqrt((0.5*D_RingA-r_Ring_mean)**2 + (0.5*D_RingI-r_Ring_mean)**2)
Fg_Ring = 58.5
T = 0
L = 2*np.pi*r_Ring_mean

print(f"Radius: {r_Ring_mean} mm\nmit Abweichung: {r_Ring_std} mm ")

c = np.array([0, 0.25, 0.5, 1, 2, 4, 8])
F = np.array([[91, 92, 92, 92, 92],
              [89, 89, 90, 90, 89],
              [87, 85.5, 85.6, 87,85],
              [83, 82, 82, 82, 81.5],
              [79, 78.5, 79, 78, 78.5],
              [75.5, 76, 76, 76, 75.5],
              [73.5, 73.7, 74, 74, 73.5]])
F = F - Fg_Ring
delF_min = 1

F_means = np.mean(F, 1)
F_std = np.std(F, 1, ddof=1)
F_std = np.array([np.max([delF_min, err]) for err in F_std])
print(f"\nMean force: {F_means}\n with std {F_std}")

tension = np.array([f / (2*L) for f in F_means])
tension_error = np.array([f for f in FehlerFortpflanzung(F_means, F_std)])
print(f"Tension: {tension}\nwith error: {tension_error}")

plt.plot(c, tension)
plt.errorbar(c, tension, tension_error, ecolor='b')
plt.xlabel("Konzentration /[mmol/l]")
plt.ylabel("Oberflächenspannung /[mN/m]]")
plt.show()