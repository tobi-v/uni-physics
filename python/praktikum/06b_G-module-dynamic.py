from numpy import array, ones, pi
from util.inertia import HollowCylinder
from util.uncertainty_calculation import MeanAndStd

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

T0_steel = array([3.33, 3.02, 3.09, 2.98, 3.12])
T_steel = array([[6.04, 6.08, 5.97, 6.06, 6.32],
                 [5.00, 4.98, 4.91, 4.91, 4.92],
                 [4.06, 4.25, 4.22, 4.14, 4.34],
                 [3.46, 3.62, 3.56, 3.69, 3.69],
                 [3.37, 3.25, 3.30, 3.25, 3.23]])

T0_steel_mean, T0_steel_std = MeanAndStd(T0_steel)
T_steel_means, T_steel_stds = MeanAndStd(T_steel, axis=1)

### periods aluminum
T0_aluminum = array([7.01, 7.22, 7.02, 7.43, 7.32])
T_aluminum = array([[13.69, 14.12, 13.91, 13.99, 14.09],
                    [11.67, 11.54, 11.81, 11.80, 11.76],
                    [10.07, 9.81, 9.91, 9.87, 10.14],
                    [8.50, 8.51, 8.24, 8.65, 8.41],
                    [7.74, 7.63, 7.39, 7.85, 7.78]])

T0_aluminum_mean, T0_aluminum_std = MeanAndStd(T0_aluminum)
T_aluminum_means, T_aluminum_stds = MeanAndStd(T_aluminum, axis=1)

### periods copper
T0_copper = array([16.23, 16.09, 16.39, 16.33, 16.25])
T_copper = array([[31.77, 31.96, 31.85, 32.06, 32.04],
                    [26.18, 26.00, 26.22, 26.44, 26.56],
                    [22.04, 22.39, 22.31, 21.30, 22.09],
                    [19.02, 18.95, 18.86, 19.10, 19.02],
                    [17.34, 17.28, 17.54, 17.09, 17.18]])

T0_copper_mean, T0_copper_std = MeanAndStd(T0_copper)
T_copper_means, T_copper_stds = MeanAndStd(T_copper, axis=1)

def C(l, G_dyn, r):
  return 8*pi*l/(G_dyn*r**4)