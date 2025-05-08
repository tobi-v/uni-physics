import numpy as np

# Fadenpendel

L = 0.885
del_Maßband = 3e-3
m_Kugel = 17.4e-3
del_Waage = 0.01e-3
r_Kugel = (1.575e-2)/2
del_Schiebelehre = 0.05e-3
t = np.array([94.215, 94.221, 94.219, 94.225, 94.227, 94.226, 94.222, 94.225, 94.225, 94.247]) / 50
t_mean = np.mean(t)
t_std = np.std(t, ddof=1)

print("Zeitmessung\n--------------------")
print(f"t_mean = {t_mean} +/- {t_std}")
print(f"f = {1/t_mean}")

print("\n\nWerte für g\n-------------------")
g_ideal = (2*np.pi/t_mean)**2 * L
print(f"ideal : g={g_ideal}")

I_Kugel = (2/5)*m_Kugel*r_Kugel**2
g_phys = (2*np.pi/t_mean)**2 * (I_Kugel + m_Kugel*L**2)/(m_Kugel*L)
print(f"physikalisch : g={g_phys}")

L_eff = L*(1+2*r_Kugel**2/(5*L**2))
g_traeg = (2*np.pi/t_mean)**2 * (I_Kugel + m_Kugel*L_eff**2)/(m_Kugel*L_eff)
print(f"Korrektur Trägheitsmoment : g={g_traeg}")

phi = 5*np.pi/180
t_mean_ausl = t_mean*(1 + (phi**2)/16)
g_ausl = (2*np.pi/t_mean_ausl)**2 * (I_Kugel + m_Kugel*L_eff**2)/(m_Kugel*L_eff)
print(f"Korrektur Auslenkung : g={g_ausl}")

m_L = (4/3) * np.pi * r_Kugel**3 * 1.225
t_mean_auftr = t_mean/np.sqrt(1 - m_L/m_Kugel)
g_auftr = (2*np.pi/t_mean_auftr)**2 * (I_Kugel + m_Kugel*L_eff**2)/(m_Kugel*L_eff)
print(f"Korrektur Auftrieb : g={g_auftr}")

dgdl = (2*np.pi/t_mean)**2
dgdt = 8*L*np.pi**2/t_mean**3
del_g = np.sqrt((dgdl*del_Maßband)**2 + (dgdt*t_std)**2)
print(f"\ng = {g_ideal} +/- {del_g}")

# Rollpendel

r_Zylinder = 1e-2
r_HohlzylinderI = 1.3e-2
r_HohlzylinderA = 1.5e-2
r_Rollkugel = 1e-2
m_Zylinder = 12.11e-3
m_Hohlzylinder = 5.71e-3
m_Rollkugel = 32.2e-3
h_Uhrglas = 2.25e-2
d_Uhrglas = 29.75e-2
R_Uhrglas = (d_Uhrglas**2 + 4*h_Uhrglas**2) / (8*h_Uhrglas)
print(f"Uhrglasradius: {R_Uhrglas}")

I_Rollkugel = (2/5) * m_Rollkugel * r_Rollkugel**2
I_Zylinder = (1/2) * m_Zylinder * r_Zylinder**2
I_Hohlzylinder = (1/2) * m_Hohlzylinder *(r_HohlzylinderA**2 + r_HohlzylinderI**2)
print("\nTrägheitsmomente\n--------------")
print(f"Kugel: {I_Rollkugel}\nZylinder: {I_Zylinder}\nHohlzylinder: {I_Hohlzylinder}")

t_Rollkugel = np.array([8.40, 8.38, 8.37, 8.32, 8.43]) / 5
t_Rollkugel_mean = np.mean(t_Rollkugel)
t_Rollkugel_std = np.std(t_Rollkugel, ddof=1)
R_Uhrglas_T = r_Rollkugel + 5*g_ideal*t_Rollkugel_mean**2/(28*np.pi**2)
dRdr = 1
dRdT = 5*g_ideal*t_Rollkugel_mean/(14*np.pi**2)
dRdg = 5*t_Rollkugel_mean**2 / (28*np.pi**2)
del_R = np.sqrt((dRdr*del_Schiebelehre)**2 + (dRdg*del_g)**2 + (dRdT*t_Rollkugel_std)**2)
print("\nRadiusbestimmung durch Perioden\n-------------------------")
print(f"T = {t_Rollkugel_mean} +/- {t_Rollkugel_std}")
print(f"Uhrglasradius R = {R_Uhrglas_T} +/- {del_R}")

def I(t, m, r, g, R):
    return m*r**2 * ((g*t**2) / (4*np.pi**2*(R-r)) - 1)

def dIdg(t, m, r, g, R):
    return m*r**2 * (t**2) / (4*np.pi**2*(R-r))

def dIdT(t, m, r, g, R):
    return m*r**2 * (2*g*t) / (4*np.pi**2*(R-r))

def dIdR(t, m, r, g, R):
    return m*r**2 * ((2*g*t) / (4*np.pi**2*(R-r)**2))

def dIdr(t, m, r, g, R):
    return 2*m*r * ((2*g*t) / (4*np.pi**2*(R-r)**2) - 1) + m*r**2 * (g*t**2) / (4*np.pi**2*(R-r))

t_Zylinder = np.array([8.67, 8.68, 8.65, 8.6, 8.68]) / 5
t_Zylinder_mean = np.mean(t_Zylinder)
t_Zylinder_std = np.std(t_Zylinder, ddof=1)
I_Zylinder_T = I(t_Zylinder_mean, m_Zylinder, r_Zylinder, g_ideal, R_Uhrglas_T)
t_Hohlzylinder = np.array([9.71, 9.5, 9.49, 9.73, 9.67]) / 5
t_Hohlzylinder_mean = np.mean(t_Hohlzylinder)
t_Hohlzylinder_std = np.std(t_Hohlzylinder, ddof=1)
I_Hohlzylinder_T = I(t_Hohlzylinder_mean, m_Hohlzylinder, r_HohlzylinderA, g_ideal, R_Uhrglas_T)

print("\nAus Periodendauer bestimmte Trägheitsmomente\n-------------------")
print(f"Zylinder: {I_Zylinder_T}")
print(f"Hohlzylinder: {I_Hohlzylinder_T}")

dIdm_Zyl = I(t_Zylinder_mean, 1, r_Zylinder, g_ideal, R_Uhrglas_T)
dIdg_Zyl = dIdg(t_Zylinder_mean, m_Zylinder, r_Zylinder, g_ideal, R_Uhrglas_T)
dIdT_Zyl = dIdT(t_Zylinder_mean, m_Zylinder, r_Zylinder, g_ideal, R_Uhrglas_T)
dIdR_Zyl = dIdR(t_Zylinder_mean, m_Zylinder, r_Zylinder, g_ideal, R_Uhrglas_T)

dIdM_HZ = I(t_Hohlzylinder_mean, 1, r_HohlzylinderA, g_ideal, R_Uhrglas_T)
dIdg_HZ = dIdg(t_Hohlzylinder_mean, m_Hohlzylinder, r_HohlzylinderA, g_ideal, R_Uhrglas_T)
dIdT_HZ = dIdT(t_Hohlzylinder_mean, m_Hohlzylinder, r_HohlzylinderA, g_ideal, R_Uhrglas_T)
dIdR_Zyl = dIdR(t_Hohlzylinder_mean, m_Hohlzylinder, r_HohlzylinderA, g_ideal, R_Uhrglas_T)