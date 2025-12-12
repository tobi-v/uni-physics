from numpy import arcsin, array

### 3.1 Vorbereitung
d_magnet = 0.02
h_magnet = 0.004
m_magnet = 0.02805/3
m_magnet_klein = 0.00168
m_ausgleich = 0.02951
m_Auto = 0.02765
#B_magnet = 

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
h = 
t_ungebremst_mittelwinkel = array([])  # Ausgleichsgew für 3 Magn
t_gebremst = array([])    # 3 Magneten
h = 0.36
t_ungebremst = array([0.393, 0.395, 0.397, 0.395, 0.393, 0.392])  # Ausgleichsgew für 3 Magn
t_gebremst = array([2.316, 2.309, 2.304, 2.29, 2.285, 2.282])    # 3 Magneten
h = 0.43
t_ungebremst = array([0.352, 0.358, 0.352, 0.361, 0.35, 0.351])  # Ausgleichsgew für 3 Magn
t_gebremst = array([1.914, 1.897, 1.899, 1.892, 1.904, 1.9])    # 3 Magneten

### 3.3.2 Abhängigkeit von der Blechdicke

t_gebremst_2mm = array([])
t_gebremst_3mm = array([])

### 3.3.3 Abhängigkeicht von der Feldstärke

t_gebremst_2magnete = array([])
t_gebremst_1magnet = array([])

### 3.3.4