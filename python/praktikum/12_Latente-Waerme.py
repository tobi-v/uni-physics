from numpy import array
from thermo.specific_heat import CMeltIce, CSteamCondensation, CSteamCondensationElectric, SpecificHeat, WaterEquivalent
import matplotlib.pyplot as plt

uncertainty = True
delT = 0.1
delM = 0.01e-3

### Part1: Water Equivalent
WE_t1 = [0,    30,   60,   90,   120,  150,  180,  190,  200,  210,  220,  230,  240,  270,  300,  330,  360]
WE_T1 = array([20.5, 20.5, 20.5, 20.5, 20.5, 20.5, 20.5, 27.6, 27.6, 27.6, 27.6, 27.6, 27.6, 27.5, 27.5, 27.5, 27.64]) + 273.15
WE_t2 = [0,    30,   60,   90,   120,  150,  180,  190,  200,  210,  220,  230,  240,  270,  300,  330,  360]
WE_T2 = array([21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 28.8, 28.9, 28.9, 28.9, 28.9, 28.9, 28.9, 28.9, 28.9, 28.8, 28.8]) + 273.15

WEfig, WEaxs = plt.subplots(2, 1)
WEaxs[0].set_title("1. Durchlauf")
WEaxs[0].plot(WE_t1, WE_T1)
WEaxs[1].set_title("2. Durchlauf")
WEaxs[1].plot(WE_t2, WE_T2)

WE_T_H1 = 35.1 + 273.15
WE_T_K1 = 20.5 + 273.15
WE_T_M1 = 27.6 + 273.15
WE_m_H1 = 104.12e-3
WE_m_K1 = 85.65e-3
WE_T_H2 = 35.1 + 273.15
WE_T_K2 = 21.0 + 273.15
WE_T_M2 = 28.9 + 273.15
WE_m_H2 = 96.04e-3
WE_m_K2 = 53.72e-3

C_D1 = WaterEquivalent(WE_T_H1, WE_T_K1, WE_T_M1, WE_m_H1, WE_m_K1)
C_D2 = WaterEquivalent(WE_T_H2, WE_T_K2, WE_T_M2, WE_m_H2, WE_m_K2)
C_D = (C_D1 + C_D2) / 2
delC_D = 0
print(f"Wasserwert1: {C_D1}\nWasserwert2: {C_D2}\nWasserwert Mittelwert: {C_D}")

### Part2: Melting Heat
CM_t1 = [0,    30,   60,   90,   120,  150,  180,  210,  240,  250,  260,  270,  280,  290,  300,  330,  360,  390,  420,  450,  480]
CM_T1 = array([41.7, 41.3, 41.1, 40.9, 40.7, 40.6, 40.4, 40.1, 40.0, 23.8, 22.8, 25.2, 25.4, 25.4, 25.4, 25.4, 25.5, 25.5, 25.5, 25.5, 25.6]) + 273.15
CM_t2 = [0,    30,   60,   90,   120,  150,  180,  210,  240,  250,  260,  270,  280,  290,  300,  330,  360,  390,  420,  450,  480]
CM_T2 = array([45.3, 45.2, 45.0, 45.0, 45.0, 44.8, 44.7, 44.7, 44.6, 34.7, 28.9, 28.7, 34.6, 35.0, 35.0, 35.0, 35.0, 35.0, 35.0, 35.0, 35.0]) + 273.15
CM_T_H1 = 40 + 273.15
CM_T_M1 = 25.5 + 273.15
CM_m_W1 = 76.15e-3
CM_m_K1 = 13.75e-3
CM_T_H2 = 44.6 + 273.15
CM_T_M2 = 35 + 273.15
CM_m_W2 = 164.35e-3
CM_m_K2 = 16.77e-3
C_melt1 = CMeltIce(CM_T_H1, CM_T_M1, CM_m_W1, CM_m_K1, C_D)
C_melt2 = CMeltIce(CM_T_H2, CM_T_M2, CM_m_W2, CM_m_K2, C_D)
C_melt = (C_melt1 + C_melt2) / 2
print(f"\nSchmelzenthalpie1: {C_melt1}\nSchmelzenthalpie2: {C_melt2}\nSchmelzenthalpie Mittelwert: {C_melt}")

CMfig, CMaxs = plt.subplots(2, 1)
CMaxs[0].set_title("1. Durchlauf CM")
CMaxs[0].plot(CM_t1, CM_T1)
CMaxs[1].set_title("2. Durchlauf CM")
CMaxs[1].plot(CM_t2, CM_T2)

### Part3: Condensation Heat
CB1_t1 = [0,    30,   60,   90,   120,  140,  150,  160,  170,  180,  190,  200,  210,  220,  230,  240,  270,  300,  330,  360]
CB1_T1 = array([21.4, 21.4, 21.4, 21.4, 21.4, 26.6, 23.7, 23.4, 23.5, 24.0, 24.1, 24.4, 25.2, 26.1, 28.0, 29.3, 31.0, 31.2, 31.3, 32.0]) + 273.15
CB1_t2 = [0,    30,   40,   50,   60,   70,   80,   90,   100,  110,  120,  130,  140,  150,  180,  210,  240,  270]
CB1_T2 = array([21.0, 22.2, 24.7, 27.3, 30.7, 33.9, 36.1, 38.6, 40.4, 43.1, 45.7, 48.6, 51.2, 54.4, 54.4, 54.5, 55.0, 55.0]) + 273.15

CB1_T_K1 = 21.4 + 273.15
CB1_T_M1 = 31 + 273.15
CB1_m_D1 = 4.9e-3
CB1_m_K1 = 201.46e-3
CB1_T_K2 = 21 + 273.15
CB1_T_M2 = 55 + 273.15
CB1_m_D2 = 14.16e-3
CB1_m_K2 = 219.04e-3

C_boil1 = CSteamCondensation(CB1_T_K1, CB1_T_M1, CB1_m_K1, CB1_m_D1, C_D)
C_boil2 = CSteamCondensation(CB1_T_K2, CB1_T_M2, CB1_m_K2, CB1_m_D2, C_D)
C_boil = (C_boil1 + C_boil2) / 2
print(f"\nKondensationsenergie1: {C_boil1}\nKondensationsenergie2: {C_boil2}\nKondensationsenergie Mittelwert: {C_boil}")

CB1fig, CB1axs = plt.subplots(2, 1)
CB1axs[0].set_title("1. Durchlauf CB1")
CB1axs[0].plot(CB1_t1, CB1_T1)
CB1axs[1].set_title("2. Durchlauf CB1")
CB1axs[1].plot(CB1_t2, CB1_T2)
#plt.show()

### Part4: Condensation Heat with Electricity

###
U1 = 52
I1 = 1.51
t1 = 240
m_D1 = 105.09e-3 - 97.83e-3
U2 = 63
I2 = 1.8
t2 = 240
m_D2 = 108.99e-3 - 97.83e-3
U3 = 69
I3 = 2
t3 = 240
m_D3 = 111.45e-3- 97.83e-3

c_k1 = CSteamCondensationElectric(U1, I1, t1, m_D1)
c_k2 = CSteamCondensationElectric(U2, I2, t2, m_D2)
c_k3 = CSteamCondensationElectric(U3, I3, t3, m_D3)
c_k = (c_k1 + c_k2 + c_k3)/3
print(f"\nc_k1 = {c_k1}\nc_k2 = {c_k2}\nc_k3 = {c_k3}\nc_k = {c_k}")