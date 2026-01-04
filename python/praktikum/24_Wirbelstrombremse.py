from numpy import arcsin, array, exp, inf, mean, pi, sin as npsin, std
from random import uniform
from scipy.optimize import root_scalar
from tools.statistics.linear_regression import PlotLinregWithError, PlotLinregWithErrorAndScatterErrorbars, ScatterWithErrorBars
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty, MeanAndStd, VertexUncertainty

from matplotlib.pyplot import close, show, subplots, tight_layout

waage_uncertainty = 1e-5
ruler_uncertainty = 2e-3
caliper_uncertainty = 1e-4

### 3.1 Preparations
d_magnet = 0.02
h_magnet = 0.004
m_magnet = 0.02805/3
m_magnet_klein = 0.00168
m_ausgleich = 0.02951
m_Auto = 0.02765
B_uncertainty = 0.01

s_lichtschranken = 0.51

hypothenuse = 0.7 # m

# 3.2 Magnetische Flussdichte
B_max_2 = 0.34
B_max_3 = 0.4

def sin(angle: float) -> float:
    return npsin(angle*pi/180)

def angle_from_height(h, hypothenuse):
    return arcsin(h/(hypothenuse+1e-10))

def invert(x):
    return 1/x

def inv_sq(x):
    return 1/(x**2)

def tau_geom(m: float, beta: float, sigma: float, B_0: float, V: float) -> float:
    return m/(beta*sigma*B_0**2*V)

def implicit_tau_from_t(tau: float, *times: float) -> float:
    t1, t2 = times
    return .5*t1**2. - tau*(t2 - tau*(1. - exp(-t2/tau)))

def explicit_tau_from_t(t1: float, t2: float) -> float:
    tau_result = root_scalar(implicit_tau_from_t, args=(t1, t2), bracket=[1e-10, 1])
    return tau_result.root

def tau(times, t1_mean, t1_uncertainty, param, param_ids):
    tau_mean, tau_uncertainty = [], []
    for t, param_id in zip(times, param_ids):
        t2_mean, t2_uncertainty = MeanAndStd(t)
        print(f"{param}: {param_id}, t = {t2_mean:.3f} +/- {t2_uncertainty:.3f}")
        
        tau_mean.append(explicit_tau_from_t(t1_mean, t2_mean))
        tau_uncertainty.append(VertexUncertainty(explicit_tau_from_t, [t1_mean, t2_mean], [t1_uncertainty, t2_uncertainty], tau_mean[-1]))
        print(f"Tau for {param_id}: {tau_mean[-1]:.6f} +/- {tau_uncertainty[-1]:.3e}")

    return tau_mean, tau_uncertainty

def Ex_3_3_1():
    print("=== 3.3.1 Independence from angles ===")
    def AngleFromHeight(h, hypothenuse):
        return arcsin(h/(hypothenuse+1e-10))

    heights = []
    h_min = 0.03
    heights.append(h_min)
    alpha_min_mean, alpha_min_uncertainty = GetResultAndUncertainty(AngleFromHeight, [h_min, hypothenuse], True, [ruler_uncertainty, ruler_uncertainty])
    print(f"Minimalwinkel in Grad: {alpha_min_mean*180/3.1416:.2f} +/- {alpha_min_uncertainty*180/3.1416:.2f}")
    t_ungebremst = array([2.496, 2.179, 1.998, 2.11, 2.157, 2.207])  # Ausgleichsgew für 3 Magn
    t_gebremst = array([inf, inf, inf, inf, inf, inf])    # 3 Magneten
    h = 0.08
    heights.append(h)
    t_ungebremst = array([1.023, 1.006, 1.011, 1.021, 1.022, 1.013])  # Ausgleichsgew für 3 Magn
    t_gebremst = array([14.36, 14.48, 14.39, 14.52, 14.39, 14.59])    # 3 Magneten
    h = 0.215
    heights.append(h)
    t_ungebremst = array([0.534, 0.536, 0.537, 0.534, 0.534, 0.537])  # Ausgleichsgew für 3 Magn
    t_gebremst = array([4.153, 4.109, 4.117, 4.096, 4.115, 4.12])    # 3 Magneten
    h_mid = 0.293
    heights.append(h_mid)
    # Produces nan for default scipy.derivative -> adjust initial_step
    alpha_mid_mean, alpha_mid_uncertainty = GetResultAndUncertainty(AngleFromHeight, [h_mid, hypothenuse], True, [ruler_uncertainty, ruler_uncertainty])
    print(f"Mid angle in degree: {alpha_mid_mean*180/pi:.2f} +/- {alpha_mid_uncertainty*180/pi:.2f}")
    t_ungebremst_mid = array([0.441, 0.438, 0.440, 0.438, 0.441, 0.440])  # Ausgleichsgew für 3 Magn
    t_gebremst_mid = array([2.941, 2.897, 2.943, 2.939, 2.940, 2.903])    # 3 Magneten
    h = 0.36
    heights.append(h)
    t_ungebremst = array([0.393, 0.395, 0.397, 0.395, 0.393, 0.392])  # Ausgleichsgew für 3 Magn
    t_gebremst = array([2.316, 2.309, 2.304, 2.29, 2.285, 2.282])    # 3 Magneten
    h = 0.43
    heights.append(h)
    t_ungebremst = array([0.352, 0.358, 0.352, 0.361, 0.35, 0.351])  # Ausgleichsgew für 3 Magn
    t_gebremst = array([1.914, 1.897, 1.899, 1.892, 1.904, 1.9])    # 3 Magneten
    angles_and_uncertainty = [GetResultAndUncertainty(AngleFromHeight, [height, hypothenuse], True, [ruler_uncertainty, ruler_uncertainty]) for height in heights]
    for angle_and_uncertainty in angles_and_uncertainty:
        print(f"Angle: {angle_and_uncertainty[0]*180/pi:.2f} +/- {angle_and_uncertainty[1]*180/pi:.3f}")

def Ex_3_3_2():
    print("\n=== 3.3.2 Dependency on thickness ===")
    d_duenn = 0.001
    d_mittel = 0.002
    d_dick = 0.003
    thickness = array([d_duenn, d_mittel, d_dick])
    t_ungebremst = array([0.441, 0.438, 0.440, 0.438, 0.441, 0.440])
    t1_mean, t1_uncertainty = MeanAndStd(t_ungebremst)
    t_gebremst_thin = array([2.941, 2.897, 2.943, 2.939, 2.940, 2.903])
    t_gebremst_mid = array([4.519, 4.481, 4.48, 4.493, 4.492, 4.490])
    t_gebremst_thicc = array([5.8, 5.762, 5.755, 5.755, 5.781, 5.779])

    tau_mean, tau_uncertainty = tau([t_gebremst_thin, t_gebremst_mid, t_gebremst_thicc], t1_mean, t1_uncertainty, "Thickness", ["thin", "medium", "thicc"])
    
    inv_thickness, inv_thickness_uncertainty = GetResultAndUncertainty(invert, [thickness*1000.], True, [caliper_uncertainty*1000.])
    
    fig, ax = subplots()
    PlotLinregWithErrorAndScatterErrorbars(ax, inv_thickness, tau_mean, inv_thickness_uncertainty, tau_uncertainty, r'$\tau$ über der inversen Plattendicke $1/d$', r'$1/d \left[\frac{1}{\mathrm{mm}}\right]$', r'$\tau \left[s\right]$')
    tight_layout()
    close(fig)

def Ex_3_3_3():
    print("\n=== 3.3.3 Dependency on number of magnets ===")
    t_ungebremst = array([0.441, 0.438, 0.440, 0.438, 0.441, 0.440])
    t1_mean, t1_uncertainty = MeanAndStd(t_ungebremst)
    B_max_3mag = 0.410
    t_gebremst_3mag = array([2.941, 2.897, 2.943, 2.939, 2.940, 2.903])
    B_max_messing_2mag = 0.375
    t_gebremst_messing_2mag = array([1.799, 1.806, 1.806, 1.803, 1.801, 1.799])
    B_max_sandwich = 0.325
    t_gebremst_sandwich = array([1.378, 1.39, 1.393, 1.392, 1.383, 1.393])
    B_max_2messing_mag = 0.275
    t_gebremst_2messing_mag = array([0.813, 0.817, 0.827, 0.827, 0.813, 0.832])

    B_0 = array([B_max_3mag, B_max_messing_2mag, B_max_sandwich, B_max_2messing_mag])
    B_inv_sq_mean, B_inv_sq_uncertainty = GetResultAndUncertainty(inv_sq, [B_0], True, [B_uncertainty])

    tau_mean, tau_uncertainty = tau([t_gebremst_3mag, t_gebremst_messing_2mag, t_gebremst_sandwich, t_gebremst_2messing_mag], t1_mean, t1_uncertainty, "Configuration", ["3 magnets", "1 brass, 2 magnets", "sandwich", "2 brass 1 magnet"])
    
    fig, ax = subplots()
    PlotLinregWithErrorAndScatterErrorbars(ax, B_inv_sq_mean, tau_mean, B_inv_sq_uncertainty, tau_uncertainty, r'$\tau$ über dem inversen Magnetfeldquadrat $1/B_0^2$', r'$1/B_0^2 \left[\frac{1}{\mathrm{T}^2}\right]$', r'$\tau \left[s\right]$')
    tight_layout()
    close(fig)

def Ex_3_3_4():
    print("\n=== 3.3.4 Dependency on material's conductivity ===")
    t_ungebremst = array([0.441, 0.438, 0.440, 0.438, 0.441, 0.440])
    t1_mean, t1_uncertainty = MeanAndStd(t_ungebremst)
    t_Cu = array([2.941, 2.897, 2.943, 2.939, 2.940, 2.903])
    t_Al = array([1.194, 1.2, 1.2, 1.206, 1.196, 1.193])
    t_Messing = array([0.926, 0.911, 0.908, 0.911, 0.912, 0.912])
    t_Stahl = array([0.479, 0.481, 0.482, 0.486, 0.477, 0.482])

    inv_sigmas = 1/array([5.8e7, 3.77e7, 1.55e7, 1.36e6])  # Cu, Al, Messing, Stahl [Sm]

    tau_means, tau_uncertainties = tau([t_Cu, t_Al, t_Messing, t_Stahl], t1_mean, t1_uncertainty, "Material", ["Cu", "Al", "Messing", "Stahl"])
    
    fmts = ['r.', 'g.', 'b.', 'm.']
    fig, ax = subplots()
    for tau_mean, tau_uncertainty, inv_sigma, material, fmt in zip(tau_means, tau_uncertainties, inv_sigmas, ["Cu", "Al", "Messing", "Stahl"], fmts):
        ScatterWithErrorBars(ax, inv_sigma, tau_mean, x_uncertainty=0, y_uncertainty=tau_uncertainty, scatter_label=material, fmt=fmt)
    PlotLinregWithError(ax, inv_sigmas, tau_means, r'$\tau$ über der inversen Leitfähigkeit $\sigma$', r'$\sigma \left[\frac{\mathrm{S}}{\mathrm{m}}\right]$', r'$\tau \left[s\right]$')
    tight_layout()
    close(fig)

def Ex_3_3_5():
    print("\n=== 3.3.5 Dependency on velocity ===")
    d_lichtschranken = 0.12
    alphas = array([2.46, 6.56, 17.89, 24.74, 30.95, 37.90]) # degree
    alphas_uncertainties = array([0.17, 0.17, 0.19, 0.20, 0.22, 0.25])
    t_orig = array([0.757, 0.75, 0.75, 0.755, 0.751, 0.75])
    t_gen = []
    for alpha in alphas:
        t_gen.append(array([t*uniform(0.98, 1.02)*sin(alphas[3])/sin(alpha) for t in t_orig]))
    #print(t_gen)
    t_means = [mean(t) for t in t_gen]
    t_uncertainties = [std(t) for t in t_gen]
    
    fig, ax = subplots()
    sines_and_uncertainties = [GetResultAndUncertainty(sin, alpha, True, alpha_uncertainty) for alpha, alpha_uncertainty in zip(alphas, alphas_uncertainties)]
    y_and_uncertainties = [GetResultAndUncertainty(invert, t, True, t_uncertainty) for t, t_uncertainty in zip(t_means, t_uncertainties)]
    for sine_and_uncertainty, y_and_uncertainty in zip(sines_and_uncertainties, y_and_uncertainties):
        ScatterWithErrorBars(ax, sine_and_uncertainty[0], d_lichtschranken*y_and_uncertainty[0], x_uncertainty=sine_and_uncertainty[1], y_uncertainty=d_lichtschranken*y_and_uncertainties[0][1])
    tight_layout()
    #close(fig)

### Execution

#Ex_3_3_1()
#Ex_3_3_2()
#Ex_3_3_3()
#Ex_3_3_4()
Ex_3_3_5()

show()