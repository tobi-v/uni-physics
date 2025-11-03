from numpy import array, linspace, float64
from numpy.typing import NDArray
from scipy.integrate import solve_ivp

import matplotlib.pyplot as plt

def Azimutalbeschleunigung(y: NDArray[float64], accel) -> NDArray[float64]:
    """Bewegungsgleichungen azimutal beschleunigte Bewegung

    Args:
        y (NDArray[float64]): Der aktuelle Zustand des Systems [rho, v, phi, omega].
        accel (float): Azimutalbeschleunigung

    Returns:
        NDArray[float64]: Die Ableitungen [drho_dt, dv_dt, dphi_dt, domega_dt].
    """
    rho, v, phi, omega = y
    drho_dt = v
    dv_dt = rho*omega**2
    dphi_dt = omega
    domega_dt = (2*v*omega - accel) / rho
    return array([drho_dt, dv_dt, dphi_dt, domega_dt])

def SimulateAcceleration(rho0: float, v0: float, phi0:float, omega0: float, t_span: tuple[float, float], t_eval: NDArray[float64], accel):
    """Simuliert die Bewegung der azimuthal beschleunigten Bewegung

    Args:
        rho0 (float): Abstand vom Ursprung [m]
        v0 (float): Anfangsgeschwindigkeit in Radialrichtung[m/s]
        phi0 (float): Anfangswinkel
        omega0 (float): Anfangsgeschwindigkeit in Radiant/s.
        t_span (tuple[float, float]): Zeitspanne für die Simulation (t0, tf).
        t_eval (NDArray[float64]): Zeitpunkte, an denen die Lösung ausgewertet wird.

    Returns:
        OdeResult: Ergebnis der Integration mit Zeitpunkten und Zuständen.
    """
    y0 = array([rho0, v0, phi0, omega0])
    solution = solve_ivp(Azimutalbeschleunigung, t_span, y0, t_eval=t_eval, method='RK45', args=(1.0,))
    return solution

t_eval = linspace(0, 10, 1000)
starts = [(1.0, 0.0, 0.0, 0.0),
          (100.0, 0.0, 0.0, 0.0),
          (100.0, 20.0, 3.14, 1.0),
          (100, 2.0, 0.0, 0.0)]

accel = 1.0

fig, axs = plt.subplots(2, 2)
for ax, (rho0, v0, phi0, omega0) in zip(axs.ravel(), starts):
    sol = SimulateAcceleration(rho0, v0, phi0, omega0, (0, 10), t_eval, accel)
    ax.plot(sol.y[0], sol.y[2], '-')
    ax.set_title(r'$\rho_0=%.2f, v_0=%.2f, \phi_0=%.2f, \omega_0=%.2f$' % (rho0, v0, phi0, omega0))
    ax.set_xlabel(r'\rho (m)')
    ax.set_ylabel(r'\phi (rad)')
    ax.grid(visible=True)

plt.tight_layout()
plt.show()