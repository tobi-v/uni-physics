from util import cylinder, inertia, feather
from util.uncertainty_calculation import GaussianErrorPropagation

from numpy import pi

g = 9.81
rho_rod = 7.7*1000  # kg/m³

error_scale = 0.01e-3
error_caliper = 0.05e-3
error_ruler = 2e-3

cylinder1_m = 284.7e-3
cylinder1_h = 5e-2
cylinder1_pos = 48.5e-2
cylinder1_r = 1.5e-2
mount1_m = 30.52e-3
mount1_pos1 = 44.6e-2
mount1_pos2 = 40.2e-2
mount1_pos3 = 35e-2
screw1_m = 2.11e-3
screw1_pos = 51.2e-2
rod1_l = 51.5e-2
rod1_d = 6.1e-3
rod1_m, delRod1_m = cylinder.MassFromVolume(rod1_l, (rod1_d/2), rho_rod, True, error_ruler, error_caliper, error_caliper)
pendulum1_m = cylinder1_m + mount1_m + screw1_m + rod1_m

cylinder2_m = 284.92e-3
cylinder2_h = 5e-2
cylinder2_pos = 48.3e-2
cylinder2_r = 1.5e-2
mount2_m = 30.39e-3
mount2_pos1 = 45e-2
mount2_pos2 = 40.5e-2
mount2_pos3 = 35.6e-2
screw2_m = 2.7e-3
screw2_pos = 51e-2
rod2_l = 51.5e-2
rod2_d = 6.1e-3
rod2_m, delRod2_m = cylinder.MassFromVolume(rod2_l, (rod2_d/2), rho_rod, True, error_ruler, error_caliper, error_caliper)

### Geometric calculation of inertia

cylinder1_J, delCylinder1_J = inertia.CylinderXY(cylinder1_m, cylinder1_pos, cylinder1_r, True, error_scale, error_ruler, error_caliper)
cylinder1_J, delCylinder1_J = inertia.Steiner(cylinder1_J, cylinder1_m, cylinder1_pos, True, delCylinder1_J, error_scale, error_ruler)
rod1_J, delRod1_J = inertia.Rod(rod1_m, rod1_l, True, error_scale, error_ruler)
rod1_J, delRod1_J = inertia.Steiner(rod1_J, rod1_m, rod1_l/2, True, error_scale, error_ruler)
screw1_J, delScrew1_J = inertia.Steiner(0, screw1_m, screw1_pos, True, error_scale, error_ruler)
mount1_J, delMount1_J = inertia.Steiner(0, mount1_m, mount1_pos1, True, error_scale, error_ruler)

J1_total = cylinder1_J + rod1_J + screw1_J + mount1_J
delJ1_total = delCylinder1_J + delRod1_J + delScrew1_J + delMount1_J

geometric_inertia_point = [cylinder1_m, cylinder1_pos, cylinder1_r]
geometric_inertia_uncertainties = [error_scale, error_ruler, error_caliper]
geometric_inertia_propagadet_error = GaussianErrorPropagation(inertia.CylinderXY, geometric_inertia_point, geometric_inertia_uncertainties)

print(f"Trägheitsmoment aus geometrischen Überlegungen: {J1_total} +/- {delJ1_total} kg*m²")

cylinder2_J, delCylinder2_J = inertia.CylinderXY(cylinder2_m, cylinder2_pos, cylinder2_r, True, error_scale, error_ruler, error_caliper)
cylinder2_J, delCylinder2_J = inertia.Steiner(cylinder2_J, cylinder2_m, cylinder2_pos, True, error_scale, error_ruler)
rod2_J, delRod2_J = inertia.Rod(rod2_m, rod2_l, True, error_scale, error_ruler)
rod2_J, delRod2_J = inertia.Steiner(rod2_J, rod2_m, rod2_l/2, True, error_scale, error_ruler)
screw2_J, delScrew2_J = inertia.Steiner(0, screw2_m, screw2_pos, True, error_scale, error_ruler)
mount2_J, delMount2_J = inertia.Steiner(0, mount2_m, mount2_pos2, True, error_scale, error_ruler)

J2_total = cylinder2_J + rod2_J + screw2_J + mount2_J
delJ2_total = delCylinder2_J + delRod2_J + delScrew2_J + delMount2_J

print(f"Trägheitsmoment aus geometrischen Überlegungen: {J2_total} +/- {delJ2_total} kg*m²")

### Determination of inertia via period

total_time = 14.7 - 1.1
num_oscillations = 10
measured_period = total_time / num_oscillations

print(f"Periodendauer des Pendels: {measured_period} s")

### Bestimmung der Federkonstante

# TODO: Die Werte stimmen nicht. Die korrekten Werte müssen noch aus dem Protokoll eingetragen werden
displacement_left = 8e-3
start_right = 4e-2
displacement_right = 7e-3
print(f"{error_ruler}\n{delRod2_m}\n{error_scale}\n")
k, k_uncertainty = feather.FeetherConstantOfCoupledPendulum(displacement_left, start_right, displacement_right, rod2_l, rod2_m, cylinder2_m, True,
                                                 error_ruler/4, error_ruler/4, error_ruler/4 , error_ruler/4, delRod2_m, error_scale)#error_ruler/4, error_ruler/4, error_ruler/4, error_ruler/40, , )

print(f"1. Die experimentell bestimmte Federkonstante beträgt {k} +/- {k_uncertainty} N/m")

### Bestimmung der Schwerpunktslänge

l_from_period = g*measured_period**2 / (4*pi**2)
print(f"2. Die aus der Periode bestimmte Schwerpunktslänge beträgt {l_from_period} m")

### Measurement opposite in phase (read from diagram)
num_oscillations = 10
time_high = 13.0
time_mid = 12.75
time_low = 12.5

period_opposite_phase_high = time_high / num_oscillations
period_opposite_phase_mid = time_mid / num_oscillations
period_opposite_phase_low = time_low / num_oscillations

### Measurement in phase (read from diagram)
num_oscillations = 10
time_high = 13.5
time_mid = 13.5
time_low = 13.5

period_in_phase = time_high / num_oscillations

### Measurement Beat Frequency (read from diagram)
beatperiod_high = 86
beatground_high = 30.5/24
beatperiod_mid = 52
beatground_mid = 19.5/15
beatperiod_low = 38
beatground_low = 19/14

### Degree of Coupling from in phase and opposite phase periods
def DegreeOfCouplingPhase(t_inPhase, t_oppositePhase):
  return (t_inPhase**2 - t_oppositePhase**2)/(t_inPhase**2 + t_oppositePhase**2)

Kphase_high = DegreeOfCouplingPhase(period_in_phase, period_opposite_phase_high)
Kphase_mid = DegreeOfCouplingPhase(period_in_phase, period_opposite_phase_mid)
Kphase_low = DegreeOfCouplingPhase(period_in_phase, period_opposite_phase_low)

print("3. Kopplungsstärken aus gleich- und gegenphasiger Schwingung:\n" \
      f"\tOben: K={Kphase_high}, Mitte: K={Kphase_mid}, Unten: K={Kphase_low}")

### Degree of coupling from beat frequency
def DegreeOfCouplingBeat(period, beat_period):
  return 2*period*beat_period/(period**2 + beat_period**2)

Kbeat_high = DegreeOfCouplingBeat(beatground_high, beatperiod_high)
Kbeat_mid = DegreeOfCouplingBeat(beatground_mid, beatperiod_mid)
Kbeat_low = DegreeOfCouplingBeat(beatground_low, beatperiod_low)

print("\tKopplungsstärken aus Schwebungsperiode:\n" \
      f"\tOben: K={Kbeat_high}, Mitte: K={Kbeat_mid}, Unten: K={Kbeat_low}")

### Inertia from period
def IfromPeriod(period, mass, length):
  return period**2 *mass*g*length / (4*pi**2)

I_high = IfromPeriod(beatground_high, pendulum1_m, l_from_period)
I_mid = IfromPeriod(beatground_mid, pendulum1_m, l_from_period)
I_low = IfromPeriod(beatground_low, pendulum1_m, l_from_period)

print("4. Aus der periode bestimmte Trägheitsmomente:\n" \
      f"\tOben: I={I_high} kg*m², Mitte: I={I_mid} kg*m², Unten: I={I_low} kg*m²")