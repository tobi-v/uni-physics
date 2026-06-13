from os.path import dirname, join
from pandas import read_csv
from tools.files.conversion import save_pandas_to_latex_table
from tools.mech.impulse import impulse2D, total_impulse2D

m_green = 18.42e-3  # [kg]
m_red = 18.46e-3
m_red_smol = 9.32e-3
m_bridge = 37.2e-3
Δm = 0.01e-3

header = [
    r'$t / \si{\second}$',
    r'$p_{x}^{\text{green}}$',
    r'$p_{y}^{\text{green}}$',
    r'$p_{x}^{\text{red}}$',
    r'$p_{y}^{\text{red}}$',
    r'$p_{x}^{\text{tot}}$',
    r'$p_{y}^{\text{tot}}$',
    r'$|p|$'
]

def read(file):
    script_dir = dirname(__file__)
    csv_path = join(script_dir, file)
    data = read_csv(csv_path)
    return data

def Impulses(experiment, red_smol=False):
    data_green = read(experiment + '_massGreen.csv')
    data_red = read(experiment + '_massRed.csv')

    def compute_impulses(df, mass):        
        def row_impulse(r):
            p_x, p_y = impulse2D(mass, r.vx, r.vy)
            p_tot = total_impulse2D(p_x, p_y)
            return p_x, p_y, p_tot

        df[['p_x', 'p_y', 'p_tot']] = df.apply(lambda r: row_impulse(r), axis=1, result_type='expand')
        return df

    dg = compute_impulses(data_green, m_green)
    if red_smol:
        dr = compute_impulses(data_red, m_red_smol)
    else:
        dr = compute_impulses(data_red, m_red)

    # combine impulses for each shared timestamp
    combined = dg[['t', 'p_x', 'p_y']].copy()
    combined = combined.rename(columns={'p_x': 'p_x_green', 'p_y': 'p_y_green'})
    combined['p_x_red'] = dr['p_x'].values
    combined['p_y_red'] = dr['p_y'].values
    combined['p_x_total'] = combined['p_x_green'] + combined['p_x_red']
    combined['p_y_total'] = combined['p_y_green'] + combined['p_y_red']
    combined['p_total'] = combined.apply(
        lambda r: total_impulse2D(r.p_x_total, r.p_y_total), axis=1
    )

    # multiply all impulse columns by 1000 (convert from kg·m/s to g·m/s) for nicer display
    combined.iloc[:, 1:] *= 1000

    save_pandas_to_latex_table(combined,
                               join(dirname(__file__), experiment + '_out_table.txt'),
                               r'Impulse des grünen und des roten Pucks, sowie der gesamte Impuls. Alle Impulsangaben in $\si{\gram\meter\per\second}$.',
                               'tab:'+experiment,
                               header)
    return

Impulses('32_01_01')
Impulses('32_01_02')
Impulses('32_02_01')
Impulses('32_02_02')
Impulses('33_01_01', red_smol=True)
Impulses('33_01_02', red_smol=True)
Impulses('33_02_01', red_smol=True)
Impulses('33_02_02', red_smol=True)
