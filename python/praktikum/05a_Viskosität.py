import numpy as np

g = 9.81
D_Rohr = 5.88e-2
R_Rohr = D_Rohr / 2
delta_Del_Rohr = 0.05e-3
d = np.array([4.98, 3.99, 2.99, 1.98])
r = (d / 2) * 10**(-3)
del_r = 0.01e-3
R = 20e-2
del_L = 0.5e-10
tlist_kugel = np.array([[4.75, 4.87, 4.81, 4.75, 4.75],
                  [7.31, 7.31, 7.31, 7.25, 7.25],
                  [12.25, 12.00, 11.87, 11.56, 11.75],
                  [25.75, 25.87, 25.75, 25.50, 25.87]])

t_ubbelohde = np.array([28.56, 27.87, 27.43, 27.37, 27.56])
k = 3.023
kin_vis = k*t_ubbelohde

mean_t = np.mean(t_ubbelohde)
std_t = np.std(t_ubbelohde, ddof=1)
print(f"Viskosiktät: {mean_t*k} +/- {k*std_t}")

