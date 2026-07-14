from matplotlib import pyplot as plt
from os.path import dirname, join
from pandas import DataFrame, read_csv
from tools.files.conversion import save_pandas_to_latex_table
from tools.mech.momentum import energy_from_momentum, momentum2D, total_momentum2D

m_green = 18.42e-3  # [kg]
m_red = 18.46e-3
m_red_smol = 9.32e-3
m_bridge = 37.2e-3
m_br_red = m_bridge/2
m_br_yellow = m_bridge/2
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
header03 = [
    r'$t / \si{\second}$',
    # r'$p_x$',
    # r'$p_y$',
    r'$|p|$',
    r'$L$',
    # r'$E_\mathrm{kin}$',
    # r'$E_\mathrm{rot}$',
    r'$E_\mathrm{full, tot}$'
]
header04 = [
    r'$t / \si{\second}$',
    # r'$p_\mathrm{Hantel}$',
    # r'$L_\mathrm{Hantel}$',
    # r'$E_\mathrm{kin,Hantel}$',
    # r'$E_\mathrm{rot,Hantel}$',
    # r'$p_\mathrm{Puck}$',
    # r'$E_\mathrm{kin,Puck}$',
    r'$p_\mathrm{tot}$',
    r'$L_\mathrm{tot}$',
    # r'$E_\mathrm{kin, tot}$',
    # r'$E_\mathrm{rot, tot}$',
    r'$E_\mathrm{full, tot}$'
]

def read(file):
    script_dir = dirname(__file__)
    csv_path = join(script_dir, file)
    data = read_csv(csv_path)
    return data

def compute_impulses(data, mass):        
    def row_impulse(r):
        p_x, p_y = momentum2D(mass, r.vx, r.vy)
        p_tot = total_momentum2D(p_x, p_y)
        return p_x, p_y, p_tot

    data[['p_x', 'p_y', 'p_tot']] = data.apply(lambda r: row_impulse(r), axis=1, result_type='expand')
    return data


def plot_positions(series, title):
    _, ax = plt.subplots()
    for item in series:
        ax.scatter(item['data'].x*100,
                   item['data'].y*100,
                   c=item.get('color'),
                   marker=item.get('marker', 'x'),
                   label=item['label'],
                   alpha=item.get('alpha', 1.0))
    ax.legend()
    ax.set_xlabel("x [cm]")
    ax.set_ylabel("y [cm]")
    ax.grid(visible=True)
    ax.set_title(title)
    return ax


def compute_bridge_state(data_red, data_yellow):
    impulses_red = compute_impulses(data_red, m_br_red)
    impulses_yellow = compute_impulses(data_yellow, m_br_yellow)

    bridge_com = DataFrame()
    bridge_com['x'] = (data_red.x + data_yellow.x) / 2
    bridge_com['y'] = (data_red.y + data_yellow.y) / 2
    bridge_com['vx'] = (data_red.vx + data_yellow.vx) / 2
    bridge_com['vy'] = (data_red.vy + data_yellow.vy) / 2
    bridge_com['p_x'] = m_bridge * bridge_com['vx']
    bridge_com['p_y'] = m_bridge * bridge_com['vy']
    bridge_com['p_total'] = total_momentum2D(bridge_com['p_x'], bridge_com['p_y'])

    rel_red_x = data_red.x - bridge_com['x']
    rel_red_y = data_red.y - bridge_com['y']
    rel_yellow_x = data_yellow.x - bridge_com['x']
    rel_yellow_y = data_yellow.y - bridge_com['y']

    bridge_com['L_red'] = rel_red_x * impulses_red['p_y'] - rel_red_y * impulses_red['p_x']
    bridge_com['L_yellow'] = rel_yellow_x * impulses_yellow['p_y'] - rel_yellow_y * impulses_yellow['p_x']
    bridge_com['L_total'] = bridge_com['L_red'] + bridge_com['L_yellow']

    bridge_com['I'] = (m_br_red * (rel_red_x**2 + rel_red_y**2)
                       + m_br_yellow * (rel_yellow_x**2 + rel_yellow_y**2))
    bridge_com['E_kin'] = bridge_com.apply(lambda r: energy_from_momentum(r.p_total, m_bridge), axis=1)
    bridge_com['E_rot'] = bridge_com['L_total']**2 / (2 * bridge_com['I'])
    bridge_com['E_full'] = bridge_com['E_kin'] + bridge_com['E_rot']

    return bridge_com, impulses_red, impulses_yellow


def compute_point_mass_state(impulses, mass):
    point_mass = DataFrame()
    point_mass['p_x'] = impulses['p_x']
    point_mass['p_y'] = impulses['p_y']
    point_mass['p_total'] = impulses['p_tot']
    point_mass['E_kin'] = point_mass.apply(lambda r: energy_from_momentum(r.p_total, mass), axis=1)
    return point_mass


def compute_system_state(bridge_com, data_green, green_state):
    total_mass = m_bridge + m_green
    system = DataFrame()
    system['x'] = (m_bridge * bridge_com['x'] + m_green * data_green.x) / total_mass
    system['y'] = (m_bridge * bridge_com['y'] + m_green * data_green.y) / total_mass

    system['p_x'] = bridge_com['p_x'] + green_state['p_x']
    system['p_y'] = bridge_com['p_y'] + green_state['p_y']
    system['p_total'] = total_momentum2D(system['p_x'], system['p_y'])

    rel_bridge_x = bridge_com['x'] - system['x']
    rel_bridge_y = bridge_com['y'] - system['y']
    rel_green_x = data_green.x - system['x']
    rel_green_y = data_green.y - system['y']

    system['L_bridge'] = rel_bridge_x * bridge_com['p_y'] - rel_bridge_y * bridge_com['p_x']
    system['L_green'] = rel_green_x * green_state['p_y'] - rel_green_y * green_state['p_x']
    system['L_total'] = system['L_bridge'] + system['L_green']

    system['I_total'] = (bridge_com['I']
                         + m_bridge * (rel_bridge_x**2 + rel_bridge_y**2)
                         + m_green * (rel_green_x**2 + rel_green_y**2))
    system['E_rot'] = system['L_total']**2 / (2 * system['I_total'])
    system['E_kin'] = system.apply(lambda r: energy_from_momentum(r.p_total, total_mass), axis=1)
    system['E_full'] = system['E_kin'] + system['E_rot']

    return system


def Impulses(experiment, red_smol=False):
    data_green = read(experiment + '_massGreen.csv')
    data_red = read(experiment + '_massRed.csv')

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
    combined['p_total'] = combined.apply(lambda r: total_momentum2D(r.p_x_total, r.p_y_total), axis=1)
    combined['E_kin'] = combined.apply(lambda r: energy_from_momentum(r.p_total, m_total), axis=1)

    # multiply all impulse columns by 1000 (convert from kg·m/s to g·m/s) for nicer display
    combined.iloc[:, 1:] *= 1000

    save_pandas_to_latex_table(combined,
                               join(dirname(__file__), experiment + '_out_table.txt'),
                               r'Impulse des grünen und des roten Pucks, sowie der gesamte Impuls. Alle Impulsangaben in $\si{\gram\meter\per\second}$, die Energie in $\si{\milli\joule}$.',
                               'tab:'+experiment,
                               header01, max_rows=40)
    
    plot_positions([
        {'data': data_green, 'color': 'g', 'label': 'Mittelpunkt Grüner Puck'},
        {'data': data_red, 'color': 'r', 'label': 'Mittelpunkt Roter Puck'},
    ], f"Positionen der Pucks für Versuch {experiment}")

def SingleImpulse(experiment):# Uses the green puck
    data = read(experiment + ".csv")

    impulses = compute_impulses(data, m_green)

    # combine impulses for each shared timestamp
    combined = impulses[['t', 'p_x', 'p_y']].copy()
    combined['p_total'] = combined.apply(lambda r: total_momentum2D(r.p_x, r.p_y), axis=1)
    combined['E_kin'] = combined.apply(lambda r: energy_from_momentum(r.p_total, m_green), axis=1)
    combined['θr'] = data['θr'].values

    # multiply all impulse columns by 1000 (convert from kg·m/s to g·m/s) for nicer display
    combined.iloc[:, 1:] *= 1000

    save_pandas_to_latex_table(combined,
                               join(dirname(__file__), experiment + '_out_table.txt'),
                               r'Impulse des an der Bande reflektierten Pucks. Alle Impulsangaben in $\si{\gram\meter\per\second}$, die Energie in $\si{\milli\joule}$.',
                               'tab:'+experiment,
                               header02, max_rows=40)
    
    plot_positions([
        {'data': data, 'color': 'r', 'label': 'Mittelpunkt Puck'},
    ], f"Positionen des Pucks für Versuch {experiment}")

def Bridge01(experiment):
    data_red = read(experiment + '_massRed.csv')
    data_yellow = read(experiment + '_massYellow.csv')

    bridge_com, _, _ = compute_bridge_state(data_red, data_yellow)

    # to_latex = bridge_com[['p_x', 'p_y', 'p_total', 'L_total']].copy()
    to_latex = bridge_com[['p_total', 'L_total']].copy()
    to_latex.insert(0, 't', data_red['t'].values)
    # to_latex['E_kin'] = bridge_com['E_kin']
    # to_latex['E_rot'] = bridge_com['E_rot']
    to_latex['E_full'] = bridge_com['E_full']

    to_latex.iloc[:, 1:] *= 1000

    save_pandas_to_latex_table(to_latex,
                               join(dirname(__file__), experiment + '_out_table.txt'),
                               r'Daten der frei bewegten Hantel. Alle Impulsangaben in $\si{\gram\meter\per\second}$, Drehimpulse in $\si{\gram\meter\squared\per\second}$, Energie in $\si{\milli\joule}$.',
                               'tab:'+experiment,
                               header03, max_rows=40)
    
    plot_positions([
        {'data': data_yellow, 'color': 'y', 'label': 'Mittelpunkt Gelber Puck'},
        {'data': data_red, 'color': 'r', 'label': 'Mittelpunkt Roter Puck'},
        {'data': bridge_com, 'color': 'k', 'marker': 'o', 'label': 'Schwerpunkt'},
    ], f"Positionen der Pucks für Versuch {experiment}")

def Bridge02(experiment):  # Bridge consists of red and yellow, single puck is green
    data_green = read(experiment + '_massGreen.csv')
    data_red = read(experiment + '_massRed.csv')
    data_yellow = read(experiment + '_massYellow.csv')

    bridge_com, _, _ = compute_bridge_state(data_red, data_yellow)
    impulses_green = compute_impulses(data_green, m_green)
    green_state = compute_point_mass_state(impulses_green, m_green)
    system_state = compute_system_state(bridge_com, data_green, green_state)

    combined = DataFrame()
    combined['t'] = data_green['t'].values
    # combined['p_tot_bridge'] = bridge_com['p_total'].values
    # combined['L_bridge'] = bridge_com['L_total'].values
    # combined['E_kin_bridge'] = bridge_com['E_kin'].values
    # combined['E_rot_bridge'] = bridge_com['E_rot'].values
    # combined['p_tot_green'] = green_state['p_total'].values
    # combined['E_kin_green'] = green_state['E_kin'].values
    combined['p_tot_system'] = system_state['p_total'].values
    combined['L_system'] = system_state['L_total'].values
    # combined['E_kin_system'] = system_state['E_kin'].values
    # combined['E_rot_system'] = system_state['E_rot'].values
    combined['E_full_system'] = system_state['E_full'].values

    combined.iloc[:, 1:] *= 1000

    save_pandas_to_latex_table(combined,
                               join(dirname(__file__), experiment + '_out_table.txt'),
                               r'Daten von Hantel und grünem Puck. Impulse in $\si{\gram\meter\per\second}$, Drehimpuls in $\si{\gram\meter\squared\per\second}$, Energie in $\si{\milli\joule}$.',
                               'tab:'+experiment,
                               header04, max_rows=40)
    
    plot_positions([
        {'data': data_yellow, 'color': 'y', 'label': 'Mittelpunkt Gelber Puck', 'alpha': 0.5},
        {'data': data_red, 'color': 'r', 'label': 'Mittelpunkt Roter Puck', 'alpha': 0.5},
        {'data': bridge_com, 'color': 'k', 'marker': 'o', 'label': 'Schwerpunkt Hantel'},
        {'data': data_green, 'color': 'g', 'label': 'Mittelpunkt Grüner Puck'},
    ], f"Positionen für Versuch {experiment}")

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

Bridge01('35_01_01')
Bridge01('35_01_02')

Bridge02('35_02_01')
Bridge02('35_02_02')

#plt.show()