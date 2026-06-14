from matplotlib import pyplot as plt
from os.path import dirname, join
from pandas import read_csv
from tools.files.conversion import save_pandas_to_latex_table
from tools.mech.impulse import energy_from_impulse, impulse2D, total_impulse2D

m_green = 18.42e-3  # [kg]
m_red = 18.46e-3
m_red_smol = 9.32e-3
m_bridge = 37.2e-3
Δm = 0.01e-3

header01 = [
    r'$t / \si{\second}$',
    r'$p_{x}^{\text{green}}$',
    r'$p_{y}^{\text{green}}$',
    r'$p_{x}^{\text{red}}$',
    r'$p_{y}^{\text{red}}$',
    r'$p_{x}^{\text{tot}}$',
    r'$p_{y}^{\text{tot}}$',
    r'$|p|$',
    r'$E_\mathrm{kin}$'
]
header02 = [
    r'$t / \si{\second}$',
    r'$p_x$',
    r'$p_y$',
    r'$|p|$',
    r'$E_\mathrm{kin}$',
    r'$\theta / \degree$',
]

def read(file):
    script_dir = dirname(__file__)
    csv_path = join(script_dir, file)
    data = read_csv(csv_path)
    return data

def compute_impulses(data, mass):        
    def row_impulse(r):
        p_x, p_y = impulse2D(mass, r.vx, r.vy)
        p_tot = total_impulse2D(p_x, p_y)
        return p_x, p_y, p_tot

    data[['p_x', 'p_y', 'p_tot']] = data.apply(lambda r: row_impulse(r), axis=1, result_type='expand')
    return data

def Impulses(experiment, red_smol=False):
    data_green = read(experiment + '_massGreen.csv')
    data_red = read(experiment + '_massRed.csv')
    
    def plotxy(data_green, data_red, experiment):
        _, ax = plt.subplots()
        ax.scatter(data_green.x*100, data_green.y*100, c='g', marker='x', label="Mittelpunkt Grüner Puck")
        ax.scatter(data_red.x*100, data_red.y*100, c='r', marker='x', label="Mittelpunkt Roter Puck")
        ax.legend()
        ax.set_xlabel("x [cm]")
        ax.set_ylabel("y [cm]")
        ax.grid(visible=True)
        ax.set_title(f"Positionen der Pucks für Versuch {experiment}")

    impulses_green = compute_impulses(data_green, m_green)
    if red_smol:
        impulses_red = compute_impulses(data_red, m_red_smol)
        m_total = m_green + m_red_smol
    else:
        impulses_red = compute_impulses(data_red, m_red)
        m_total = m_green + m_red

    # combine impulses for each shared timestamp
    combined = impulses_green[['t', 'p_x', 'p_y']].copy()
    combined = combined.rename(columns={'p_x': 'p_x_green', 'p_y': 'p_y_green'})
    combined['p_x_red'] = impulses_red['p_x'].values
    combined['p_y_red'] = impulses_red['p_y'].values
    combined['p_x_total'] = combined['p_x_green'] + combined['p_x_red']
    combined['p_y_total'] = combined['p_y_green'] + combined['p_y_red']
    combined['p_total'] = combined.apply(lambda r: total_impulse2D(r.p_x_total, r.p_y_total), axis=1)
    combined['E_kin'] = combined.apply(lambda r: energy_from_impulse(r.p_total, m_total), axis=1)

    # multiply all impulse columns by 1000 (convert from kg·m/s to g·m/s) for nicer display
    combined.iloc[:, 1:] *= 1000

    save_pandas_to_latex_table(combined,
                               join(dirname(__file__), experiment + '_out_table.txt'),
                               r'Impulse des grünen und des roten Pucks, sowie der gesamte Impuls. Alle Impulsangaben in $\si{\gram\meter\per\second}$, die Energie in $\si{\milli\joule}$.',
                               'tab:'+experiment,
                               header01)
    
    plotxy(data_green, data_red, experiment)

def SingleImpulse(experiment):# Uses the green puck
    data = read(experiment + ".csv")
    
    def plotxy(data, experiment):
        _, ax = plt.subplots()
        ax.scatter(data.x*100, data.y*100, c='r', marker='x', label="Mittelpunkt Puck")
        ax.legend()
        ax.set_xlabel("x [cm]")
        ax.set_ylabel("y [cm]")
        ax.grid(visible=True)
        ax.set_title(f"Positionen des Pucks für Versuch {experiment}")

    impulses = compute_impulses(data, m_green)

    # combine impulses for each shared timestamp
    combined = impulses[['t', 'p_x', 'p_y']].copy()
    combined['p_total'] = combined.apply(lambda r: total_impulse2D(r.p_x, r.p_y), axis=1)
    combined['E_kin'] = combined.apply(lambda r: energy_from_impulse(r.p_total, m_green), axis=1)
    combined['θr'] = data['θr'].values

    # multiply all impulse columns by 1000 (convert from kg·m/s to g·m/s) for nicer display
    combined.iloc[:, 1:] *= 1000

    save_pandas_to_latex_table(combined,
                               join(dirname(__file__), experiment + '_out_table.txt'),
                               r'Impulse des an der Bande reflektierten Pucks. Alle Impulsangaben in $\si{\gram\meter\per\second}$, die Energie in $\si{\milli\joule}$.',
                               'tab:'+experiment,
                               header02)
    
    plotxy(data, experiment)

Impulses('32_01_01')
Impulses('32_01_02')
Impulses('32_02_01')
Impulses('32_02_02')
Impulses('33_01_01', red_smol=True)
Impulses('33_01_02', red_smol=True)
Impulses('33_02_01', red_smol=True)
Impulses('33_02_02', red_smol=True)

SingleImpulse('34_01')
SingleImpulse('34_02')

# plt.show()