
from numpy import array, mean, ones_like, std
from tools.optics.focal_length_determination import bessel_method, d_from_serial_focal_length, f_lensmakers_equation, serial_focal_length
from tools.optics.microscope import magnification_obj

Δx = 0.2

def f_comb(f1, f2, d):
    return 1 / (1 / f1 + 1 / f2 - d / (f1 * f2))

def d_from_f(f, f1, f2):
    return (1 / f1 + 1 / f2 - 1 / f) * (f1 * f2)

def Abbildungsverfahren():
    print("=== Abbildungsverfahren ===")
    print("--- Sammellinse [6 cm] Brennweite ---")
    g1 = array([7.5, 8, 8.5, 9])
    b1 = array([30.3, 23.9, 20.7, 18.7])
    f1, Δf1 = f_lensmakers_equation(g1, b1, uncertainty=True, Δg=Δx, Δb=Δx)
    print(f"f = {mean(f1):.3f} ± {mean(Δf1):.3f} cm")

    f2_theo = serial_focal_length(6, -15)
    print(f"\n--- Linsensystem (theoretisch f={f2_theo:.3f} für d=0) ---")
    g2 = array([11, 11.5, 11.95, 12.5])
    b2 = array([32.8, 29.6, 27.6, 25.4])
    f2, Δf2 = f_lensmakers_equation(g2, b2, uncertainty=True, Δg=Δx, Δb=Δx)
    print(f"f = {mean(f2):.3f} ± {mean(Δf2):.3f} cm")
    d, Δd = d_from_serial_focal_length(mean(f2), 6, -15, uncertainty=True, Δf=mean(Δf2))
    print(f"Tatsächlicher Abstand: {d:.3f} ± {Δd:.3f} cm")

def Besselverfahren():
    print("\n=== Besselverfahren ===")
    print("--- Sammellinse [10 cm] Brennweite ---")
    a1 = array([47.8, 57, 65.5, 75])
    e1 = array([18.7, 30.2, 39, 50])
    f1, Δf1 = bessel_method(e1, a1, uncertainty=True, Δe=Δx, Δa=Δx)
    print(f"f = {mean(f1):.3f} ± {mean(Δf1):.3f} cm")

    f2_theo = serial_focal_length(6, -15)
    print(f"\n--- Linsensystem (theoretisch f={f2_theo:.3f} für d=0) ---")
    a2 = array([31, 34, 38, 41.2])
    e2 = array([4, 4.6, 10.8, 17.4])
    f2, Δf2 = bessel_method(e2, a2, uncertainty=True, Δe=Δx, Δa=Δx)
    print(f"f = {mean(f2):.3f} ± {mean(Δf2):.3f} cm")
    d, Δd = d_from_serial_focal_length(mean(f2), 6, -15, uncertainty=True, Δf=mean(Δf2))
    print(f"Tatsächlicher Abstand: {d:.3f} ± {Δd:.3f} cm")

def Autokollimation():
    print("\n=== Autokollimationsverfahren ===")
    print("--- Sammellinse [10 cm] Brennweite ---")
    f1 = array([5.5, 6.3])
    Δf1 = std(f1)
    f1 = mean(f1)
    print(f"f = {mean(f1):.3f} ± {mean(Δf1):.3f} cm")

    print("\n--- Sammellinse [10 cm] Brennweite ---")
    f2 = array([9.9, 9])
    Δf2 = std(f2)
    f2 = mean(f2)
    print(f"f = {mean(f2):.3f} ± {mean(Δf2):.3f} cm")

    f3_theo = serial_focal_length(6, -15)
    print(f"\n--- Linsensystem (theoretisch f={f3_theo:.3f} für d=0) ---")
    f3 = array([12.6, 11])
    Δf3 = std(f3)
    f3 = mean(f3)
    print(f"f = {mean(f3):.3f} ± {mean(Δf3):.3f} cm")
    d, Δd = d_from_serial_focal_length(f3, 6, -15, uncertainty=True, Δf=Δf3)
    print(f"Tatsächlicher Abstand: {d:.3f} ± {Δd:.3f} cm")

def Mikroskop():    
    print("\n=== Mikroskop ===")
    d = array([10, 10.8, 13.5, 12])
    V = array([3.3, 4, 6, 5])
    f_okk = 2.5
    f_obj = 1.6
    s_0 = 25

    V, ΔV = magnification_obj(d, f_obj*ones_like(d), uncertainty=True, Δd=Δx)
    print(f"Vergrößerungen {V}\nFehler {ΔV}")


# Abbildungsverfahren()
# Besselverfahren()
#Autokollimation()
Mikroskop()