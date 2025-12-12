from numpy import arcsin, array

### 3.1 Vorbereitung
d_magnet = 0.02
h_magnet = 0.004
m_magnet = 0.02805/3
m_magnet_klein = 0.00168
m_ausgleich = 0.02951
m_Auto = 0.02765
#B_magnet = 
B_uncertainty = 0.01

d_blech_cu =
s_lichtschranken = 0.51

hypothenuse = 0.7 # m

# 3.2 Magnetische Flussdichte
B_max_1 = 
B_max_2 = 0.34
B_max_3 = 0.4

### 3.3.1
h_alpha_min = 0.03
alpha_min = arcsin(h_alpha_min/hypothenuse)
t_ungebremst = array([2.496, 2.179, 1.998, 2.11, 2.157, 2.207])  # Ausgleichsgew für 3 Magn
t_gebremst = array([inf, inf, inf, inf, inf, inf])    # 3 Magneten
h = 0.08
t_ungebremst = array([1.023, 1.006, 1.011, 1.021, 1.022, 1.013])  # Ausgleichsgew für 3 Magn
t_gebremst = array([14.36, 14.48, 14.39, 14.52, 14.39, 14.59])    # 3 Magneten
h = 0.215
t_ungebremst = array([0.534, 0.536, 0.537, 0.534, 0.534, 0.537])  # Ausgleichsgew für 3 Magn
t_gebremst = array([4.153, 4.109, 4.117, 4.096, 4.115, 4.12])    # 3 Magneten
h = 0.293
t_ungebremst_mittelwinkel = array([0.441, 0.438, 0.440, 0.438, 0.441, 0.440])  # Ausgleichsgew für 3 Magn
t_gebremst = array([2.941, 2.897, 2.943, 2.939, 2.940, 2.903])    # 3 Magneten
h = 0.36
t_ungebremst = array([0.393, 0.395, 0.397, 0.395, 0.393, 0.392])  # Ausgleichsgew für 3 Magn
t_gebremst = array([2.316, 2.309, 2.304, 2.29, 2.285, 2.282])    # 3 Magneten
h = 0.43
t_ungebremst = array([0.352, 0.358, 0.352, 0.361, 0.35, 0.351])  # Ausgleichsgew für 3 Magn
t_gebremst = array([1.914, 1.897, 1.899, 1.892, 1.904, 1.9])    # 3 Magneten

### 3.3.2 Abhängigkeit von der Blechdicke

d_duenn = 0.001
d_mittel = 0.002
d_dick = 0.003
t_gebremst_2mm = array([4.519, 4.481, 4.48, 4.493, 4.492, 4.490])
t_gebremst_3mm = array([5.8, 5.762, 5.755, 5.755, 5.781, 5.779])

### 3.3.3 Abhängigkeicht von der Feldstärke

B_max_3mag = 0.410
B_max_messing_2mag = 0.375
t_gebremst_messing_2mag = array([1.799, 1.806, 1.806, 1.803, 1.801, 1.799])
B_max_sandwich = 0.325
t_gebremst_sandwich = array([1.378, 1.39, 1.393, 1.392, 1.383, 1.393])
B_max_2messing_mag = 0.275
t_gebremst_2messing_mag = array([0.813, 0.817, 0.827, 0.827, 0.813, 0.832])

### 3.3.4

d_Al = 0.001
t_Al = array([1.194, 1.2, 1.2, 1.206, 1.196, 1.193])
d_Messing = 0.001
t_Messing = array([0.926, 0.911, 0.908, 0.911, 0.912, 0.912])
d_Stahl = 0.001
t_Stahl = array([0.479, 0.481, 0.482, 0.486, 0.477, 0.482])

### 3.3.5

d_lichtschranken = 0.12
t = array([0.757, 0.75, 0.75, 0.755, 0.751, 0.75])