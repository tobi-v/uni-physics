from util.linear_regression import linreg, plot
import numpy as np
import matplotlib.pyplot as plt

g = 9.81
L = 0.945
r_Cu_Fe = 0.0005
r_Al = 0.001
R_disc = 0.08

def GModule(steigung, r):
    return 2*g*L*R_disc / (np.pi*steigung*r**4)

def GModuleError(steigung, r, delL, delR, delSteigung, delr):
    return np.sqrt((2*g*R_disc / (np.pi*steigung*r**4) *delL)**2+
        (2*g*L / (np.pi*steigung*r**4) *delR)**2+
        (2*g*L*R_disc / (np.pi*steigung**2*r**4) *delSteigung)**2+
        (4*2*g*L*R_disc / (np.pi*steigung*r**5)*delr)**2)


m_Cu_Fe = np.linspace(2, 20, 10)/1000
m_Al = np.linspace(8, 80, 10)/1000

rad_Fe = (np.pi/180) * np.array([1, 8, 20.5, 47, 52, 63, 67, 68, 79, 81.5])
rad_Cu = (np.pi/180) * np.array([1, 14, 17.5, 21, 42, 44, 48, 66, 72.5, 93.5])
rad_Al = (np.pi/180) * np.array([6, 13, 22.5, 30, 37, 43, 55, 65, 70, 75])

CuFun, Cu_steigung, Cu_cov = linreg(m_Cu_Fe, rad_Cu)
FeFun, Fe_steigung, Fe_cov = linreg(m_Cu_Fe, rad_Fe)
AlFun, Al_steigung, Al_cov = linreg(m_Al, rad_Al)

print(f"Kupfer Steigung: {Cu_steigung}\nStahl Steigung: {Fe_steigung}\nAluminium Steigung: {Al_steigung}")

error_Fe = np.abs(FeFun(m_Cu_Fe) - rad_Fe)
error_Fe_mean = np.mean(error_Fe)
error_Fe_std = np.std(error_Fe, ddof=1)
error_Cu = np.abs(CuFun(m_Cu_Fe) - rad_Cu)
error_Cu_mean = np.mean(error_Cu)
error_Cu_std = np.std(error_Cu, ddof=1)
error_Al = np.abs(AlFun(m_Al) - rad_Al)
error_Al_mean = np.mean(error_Al)
error_Al_std = np.std(error_Al, ddof=1)
print(f"\n\nMittlere Abweichungen:" \
      f"\nStahl: Fehler {error_Fe_mean*180/np.pi} std {error_Fe_std}"\
      f"\nKupfer: Fehler {error_Cu_mean*180/np.pi} std {error_Cu_std}" \
      f"\nAluminium: Fehler {error_Al_mean*180/np.pi} std {error_Al_std}")

Gmod_Fe = GModule(Fe_steigung, r_Cu_Fe)
Gmod_Cu = GModule(Cu_steigung, r_Cu_Fe)
Gmod_Al = GModule(Al_steigung, r_Al)
print(f"\n\nG Module:\nStahl: G={Gmod_Fe/10**9} GPa\nKupfer: G={Gmod_Cu/10**9} GPa\nAluminium: G={Gmod_Al/10**9} GPa")

GMod_Fe_error = GModuleError(Fe_steigung, r_Cu_Fe, 0.002, 0.001, np.sqrt(Fe_cov[0, 0]), 0.00001)
GMod_Cu_error = GModuleError(Cu_steigung, r_Cu_Fe, 0.002, 0.001, np.sqrt(Cu_cov[0, 0]), 0.00001)
GMod_Al_error = GModuleError(Al_steigung, r_Al, 0.002, 0.001, np.sqrt(Al_cov[0, 0]), 0.00001)

print(f"\n\nFehler GModule\nEisen: {GMod_Fe_error/10**9}\nKupfer: {GMod_Cu_error/10**9}\nAluminium: {GMod_Al_error/10**9}")

fig, axs = plt.subplots(3, 1)
plot(axs[0], m_Cu_Fe, rad_Cu, CuFun, error_Cu, "Copper")
plot(axs[1], m_Cu_Fe, rad_Fe, FeFun, error_Fe, "Steel")
plot(axs[2], m_Al, rad_Cu, AlFun, error_Al, "Aluminum")
plt.show()
