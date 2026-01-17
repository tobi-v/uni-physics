from numpy import concatenate, cross, empty_like, eye, linspace
from scipy.integrate import solve_ivp
from matplotlib.pyplot import axes, draw, show, subplots, suptitle, tight_layout
from matplotlib.widgets import CheckButtons

# (Teil a)
def euler_equations(t, ω, I):
    ω1, ω2, ω3 = ω
    I1, I2, I3 = I
    ω1_dt = ((I2 - I3) / I1) * ω2 * ω3
    ω2_dt = ((I3 - I1) / I2) * ω1 * ω3
    ω3_dt = ((I1 - I2) / I3) * ω1 * ω2
    return [ω1_dt, ω2_dt, ω3_dt]

# DGL für körperfeste Basis (Teil b)
def dn_dt(t, n, ω):
    n = n.reshape(3, 3)  # Vektor n wieder in 3x3 Form ballern 
    dn_dt_matrix = empty_like(n)

    for i in range(3):
        dn_dt_matrix[i] = cross(ω, n[i])

    return dn_dt_matrix.flatten()

# DGL für raumfeste Basis (Teil c)
def dkoerper_dt(t, ω_n, I):
    dω = euler_equations(t, ω_n[0:3], I)
    dn = dn_dt(t, ω_n[3:], ω_n[0:3])
    return concatenate((dω, dn))

I = [1.0, 1.5, 2.0]  # Beispielhafte Trägheitsmomente
ω_0 = [.5, 1., 1.5]  # Beispielhafte AB
n0 = eye(3).flatten() # Orthonormale körperfeste Basis
t_span = (0, 20)
t_eval = linspace(t_span[0], t_span[1], 1000)

def a():
    sol = solve_ivp(euler_equations, t_span, ω_0, args=(I,), t_eval=t_eval, method='RK45')

    # 3D-Plot der Winkelgeschwindigkeiten
    _, ax = subplots(subplot_kw={'projection': '3d'})
    ax.plot(sol.y[0], sol.y[1], sol.y[2], label='Winkelgeschwindigkeit')
    ax.set_xlabel(r'$\omega_1$')
    ax.set_ylabel(r'$\omega_2$')
    ax.set_zlabel(r'$\omega_3$')
    ax.set_title(r'3D-Plot der vektoriellen Winkelgeschwindigkeit $\omega$')
    ax.legend()
    show()

    # Zeitabhängiger Plot der Winkelgeschwindigkeiten
    _, axs = subplots(3, 1, figsize=(10, 8))
    for ax, y, label in zip(axs, sol.y, [r'$\omega_1$', r'$\omega_2$', r'$\omega_3$']):
        ax.plot(sol.t, y)
        ax.set_ylabel(label)
        ax.set_xlabel('Zeit [s]')
    suptitle('Zeitabhängige Winkelgeschwindigkeiten')
    tight_layout()
    show()

def b():
    sol = solve_ivp(dn_dt, t_span, n0, args=(ω_0,), t_eval=t_eval, method='RK45')

    _, ax = subplots(subplot_kw={'projection': '3d'})
    for i in range(3):
        ax.plot(sol.y[i*3], sol.y[i*3+1], sol.y[i*3+2], label=f'$\\vec{{n}}_{i+1}(t)$')
    ax.set_xlabel(r'$n_1$')
    ax.set_ylabel(r'$n_2$')
    ax.set_zlabel(r'$n_3$')
    ax.set_title(r'Bewegung der Körperachsen $\vec{n}_j(t)$ mit Konstantem ω')
    ax.legend()
    show()

def c():
    sol = solve_ivp(dkoerper_dt, t_span, concatenate((ω_0, n0)), args=(I,), t_eval=t_eval, method='RK45')
    n = sol.y[3:]

    _, ax = subplots(subplot_kw={'projection': '3d'})
    for i in range(3):
        ax.plot(n[i*3], n[i*3+1], n[i*3+2], label=f'$\\vec{{n}}_{i+1}(t)$')
    ax.set_xlabel(r'$n_1$')
    ax.set_ylabel(r'$n_2$')
    ax.set_zlabel(r'$n_3$')
    ax.set_title(r'Bewegung der Körperachsen $\vec{n}_j(t)$ mit konstantem ω')
    ax.legend()
    show()

def d():
    t_span = (0, 100)
    t_eval = linspace(t_span[0], t_span[1], 10000)
    I = [2.0, 1.5, 1.]
    ω_0s = [[1, .1, .01], [.1, 1, .01], [.1, .01, 1]] # AB fast parallel zu den Achsen ABER NUR FAST
    _, axs = subplots(3, 1,subplot_kw={'projection': '3d'})
    checkbox_positions = [0, 0.3, 0.6]
    check_buttons = []
    for ω_0, ax, pos in zip(ω_0s, axs, checkbox_positions):
        sol = solve_ivp(dkoerper_dt, t_span, concatenate((ω_0, n0)), args=(I,), t_eval=t_eval, method='RK45')
        n = sol.y[3:]

        lines = []
        for i in range(3):
            line, = ax.plot(n[i*3], n[i*3+1], n[i*3+2], label=f'$\\vec{{n}}_{i+1}(t)$')
            lines.append(line)
        ax.set_xlabel(r'$n_1$')
        ax.set_ylabel(r'$n_2$')
        ax.set_zlabel(r'$n_3$')
        ax.set_title(r'Bewegung der Körperachsen $\vec{n}_j(t)$ mit variablem ω')
        ax.legend()

        rax = axes([pos, 0.05, 0.6, 0.1])
        check_buttons.append(CheckButtons(rax, (r'$\vec{n}_1(t)$', r'$\vec{n}_2(t)$', r'$\vec{n}_3(t)$'), [True, True, True]))
        # Function to toggle visibility
        def toggle_visibility(lines):
            def inner_toggle_visibility(label):
                index = int(label[-5]) - 1  # Extract the index from the label
                lines[index].set_visible(not lines[index].get_visible())
                draw()
            return inner_toggle_visibility

        check_buttons[-1].on_clicked(toggle_visibility(lines))

    show()


#a()
#b()
#c()
d()