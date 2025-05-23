from matplotlib import pyplot as plt
from numpy import array, empty, pi, sqrt
from util.inertia import HollowCylinder
from util.uncertainty_calculation import GetResultAndUncertainty, MeanAndStd
from util.linear_regression import linreg, plotWithErrorBars

def T_i_sq_minus_T_0_sq(T_i, T_0, uncertainty=False, delT_i=0, delT_0=0):
  def T_i_sq_minus_T_0_sqInner(T_i, T_0):
    return T_i**2 - T_0**2
  return GetResultAndUncertainty(T_i_sq_minus_T_0_sqInner, [T_i, T_0], uncertainty, [delT_i, delT_0])

def GfromC(C, l, r, uncertainty=False, delC=0, delL=0, delR=0):
  def GfromCInner(C, l, r):
    return 8*pi*l/(C*r**4)
  return GetResultAndUncertainty(GfromCInner, [C, l, r], uncertainty, [delC, delL, delR])
  
uncertainty=True
textbox_props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

error_ruler = 2e-3
error_caliper = 0.01e-3
error_scale = 0.1e-3

wire_steel_d = 2.39e-3
wire_steel_l = 97.2e-2
wire_aluminum_d = 2.02e-3
wire_aluminum_l = 98e-2
wire_copper_d = 1.00e-3
wire_copper_l = 97.8e-2

ring_m = array([922.8, 738.1, 606.4, 422.4, 251.8])*10**-3
ring_d1 = array([25.8, 21.4, 16.8, 12.5, 9])*10**-2
ring_d2 = array([29.0, 25.3, 20.8, 16.2, 12])*10**-2
J, delJ = HollowCylinder(ring_m, ring_d1/2, ring_d2/2, True, error_scale, error_ruler/2, error_ruler/2)
print(f"J {J}, delJ {delJ}")

T0_steel = array([3.33, 3.02, 3.09, 2.98, 3.12])/3
T_steel = array([[6.04, 6.08, 5.97, 6.06, 6.32],
                 [5.00, 4.98, 4.91, 4.91, 4.92],
                 [4.06, 4.25, 4.22, 4.14, 4.34],
                 [3.46, 3.62, 3.56, 3.69, 3.69],
                 [3.37, 3.25, 3.30, 3.25, 3.23]])/3

T0_steel_mean, T0_steel_std = MeanAndStd(T0_steel)
T_steel_means, T_steel_stds = MeanAndStd(T_steel, axis=1)
Y_steel = empty(5)
delY_steel = empty(5)
for ii, T in enumerate(T_steel_means): # Need to loop because we have different std for each point TODO: Adjust GetResultAndUncertainty accordingly
  Y_steel[ii], delY_steel[ii]= T_i_sq_minus_T_0_sq(T, T0_steel_mean, uncertainty, T_steel_stds[ii], T0_steel_std)

C_steel_linreg_fun, C_steel_inclination, C_steel_covariance = linreg(J, Y_steel)
fig, axs = plt.subplots(nrows=3,ncols=1, figsize=(9,9))

plotWithErrorBars(axs[0], J, Y_steel, C_steel_linreg_fun, x_absErr=delJ, y_absErr=delY_steel, title="Stahl", xlabel=r'$J/kgm^2$', ylabel=r'$T_{steel}^2-T_{0,steel}^2/s^2$')
fe_textbox = r'$C_{Stahl}=%.1f \pm %.1f$' % (C_steel_inclination, C_steel_covariance[0,0])
axs[0].text(0.05, 0.95, fe_textbox, transform=axs[0].transAxes, fontsize=14, verticalalignment='top', bbox=textbox_props)

Gdyn_steel, delGdyn_steel = GfromC(C_steel_inclination, wire_steel_l, wire_steel_d/2, uncertainty, sqrt(C_steel_covariance[0, 0]), error_ruler, error_caliper/2)
print(f"\nG Modul Stahl: \t\t{Gdyn_steel/10**9} +/- {delGdyn_steel/10**9} GPa")

### periods aluminum
T0_aluminum = array([7.01, 7.22, 7.02, 7.43, 7.32])/3
T_aluminum = array([[13.69, 14.12, 13.91, 13.99, 14.09],
                    [11.67, 11.54, 11.81, 11.80, 11.76],
                    [10.07, 9.81, 9.91, 9.87, 10.14],
                    [8.50, 8.51, 8.24, 8.65, 8.41],
                    [7.74, 7.63, 7.39, 7.85, 7.78]])/3

T0_aluminum_mean, T0_aluminum_std = MeanAndStd(T0_aluminum)
T_aluminum_means, T_aluminum_stds = MeanAndStd(T_aluminum, axis=1)
Y_aluminum = empty(5)
delY_aluminum = empty(5)
for ii, T in enumerate(T_aluminum_means):
  Y_aluminum[ii], delY_aluminum[ii]= T_i_sq_minus_T_0_sq(T, T0_aluminum_mean, uncertainty, T_aluminum_stds[ii], T0_aluminum_std)

C_aluminum_linreg_fun, C_aluminum_inclination, C_aluminum_covariance = linreg(J, Y_aluminum)

al_textbox = r'$C_{Aluminium}=%.1f \pm %.1f$' % (C_aluminum_inclination, C_aluminum_covariance[0,0])
axs[1].text(0.05, 0.95, al_textbox, transform=axs[1].transAxes, fontsize=14, verticalalignment='top', bbox=textbox_props)
plotWithErrorBars(axs[1], J, Y_aluminum, C_aluminum_linreg_fun, x_absErr=delJ, y_absErr=delY_aluminum, title="Aluminium", xlabel=r'$J/kgm^2$', ylabel=r'$T_{aluminum}^2-T_{0,aluminum}^2/s^2$')

Gdyn_aluminum, delGdyn_aluminum = GfromC(C_aluminum_inclination, wire_aluminum_l, wire_aluminum_d/2, uncertainty, sqrt(C_aluminum_covariance[0, 0]), error_ruler, error_caliper/2)
print(f"\nG Modul Aluminium: \t{Gdyn_aluminum/10**9} +/- {delGdyn_aluminum/10**9} GPa")

### periods copper
T0_copper = array([16.23, 16.09, 16.39, 16.33, 16.25])/3
T_copper = array([[31.77, 31.96, 31.85, 32.06, 32.04],
                    [26.18, 26.00, 26.22, 26.44, 26.56],
                    [22.04, 22.39, 22.31, 21.30, 22.09],
                    [19.02, 18.95, 18.86, 19.10, 19.02],
                    [17.34, 17.28, 17.54, 17.09, 17.18]])/3

T0_copper_mean, T0_copper_std = MeanAndStd(T0_copper)
T_copper_means, T_copper_stds = MeanAndStd(T_copper, axis=1)
Y_copper = empty(5)
delY_copper = empty(5)
for ii, T in enumerate(T_copper_means):
  Y_copper[ii], delY_copper[ii]= T_i_sq_minus_T_0_sq(T, T0_copper_mean, uncertainty, T_copper_stds[ii], T0_copper_std)

C_copper_linreg_fun, C_copper_inclination, C_copper_covariance = linreg(J, Y_copper)

cu_textbox = r'$C_{Kupfer}=%.1f \pm %.1f$' % (C_copper_inclination, C_copper_covariance[0,0])
axs[2].text(0.05, 0.95, cu_textbox, transform=axs[2].transAxes, fontsize=14, verticalalignment='top', bbox=textbox_props)
plotWithErrorBars(axs[2], J, Y_copper, C_copper_linreg_fun,
                  x_absErr=delJ, y_absErr=delY_copper, title="Kupfer", xlabel=r'$J/kgm^2$', ylabel=r'$T_{copper}^2-T_{0,copper}^2/s^2$')

Gdyn_copper, delGdyn_copper = GfromC(C_copper_inclination, wire_copper_l, wire_copper_d/2, uncertainty, sqrt(C_copper_covariance[0, 0]), error_ruler, error_caliper/2)
print(f"\nG Modul Kupfer: \t{Gdyn_copper/10**9} +/- {delGdyn_copper/10**9} GPa")


plt.tight_layout()
plt.show()