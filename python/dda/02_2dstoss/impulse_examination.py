from os.path import dirname, join
from pandas import read_csv
from tools.mech.impulse import impulse2D, total_impulse2D

m_green = 18.42e-3  # [kg]
m_red = 18.46e-3
m_red_smol = 9.32e-3
m_bridge = 37.2e-3
Δm = 0.01e-3

def read(file):
    script_dir = dirname(__file__)
    csv_path = join(script_dir, file)
    data = read_csv(csv_path)
    return data

def Ex_32_01_01():
    data_green = read('32_01_01_massGreen.csv')
    data_red = read('32_01_01_massRed.csv')

    def compute_impulses(df, mass):        
        def row_impulse(r):
            p_x, p_y = impulse2D(mass, r.vx, r.vy)
            p_tot = total_impulse2D(p_x, p_y)
            return p_x, p_y, p_tot

        df[['p_x', 'p_y', 'p_tot']] = df.apply(lambda r: row_impulse(r), axis=1, result_type='expand')
        return df

    dg = compute_impulses(data_green, m_green)
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

    print('Green sample:')
    print(dg[['t', 'vx', 'vy', 'p_x', 'p_y', 'p_tot']].head())
    print('Red sample:')
    print(dr[['t', 'vx', 'vy', 'p_x', 'p_y', 'p_tot']].head())
    print('Combined sample:')
    print(combined[['t', 'p_x_total', 'p_y_total', 'p_total']].head())

    # TODO: Clean up a bit, output impulses in gram times velocity and round after two decimals
    tex_file = join(dirname(__file__), 'combined_impulse_table.txt')
    columns = ['t', 'p_x_green', 'p_y_green', 'p_x_red', 'p_y_red', 'p_x_total', 'p_y_total', 'p_total']
    header = [
        't',
        r'$p_{x}^{\text{green}}$',
        r'$p_{y}^{\text{green}}$',
        r'$p_{x}^{\text{red}}$',
        r'$p_{y}^{\text{red}}$',
        r'$p_{x}^{\text{tot}}$',
        r'$p_{y}^{\text{tot}}$',
        r'$|p|$'
    ]

    combined_tex = combined.copy()
    combined_tex.columns = [
        't',
        r'$p_{x}^{\text{green}}$',
        r'$p_{y}^{\text{green}}$',
        r'$p_{x}^{\text{red}}$',
        r'$p_{y}^{\text{red}}$',
        r'$p_{x}^{\text{tot}}$',
        r'$p_{y}^{\text{tot}}$',
        r'$|p|$'
    ]

    combined_tex.to_latex(
        buf=tex_file,
        index=False,
        float_format='%.6g',
        caption='Combined impulse for green and red masses',
        label='tab:combined_impulse',
        escape=False
    )

    print(f'Saved combined LaTeX table to {tex_file}')
    return dg, dr, combined

Ex_32_01_01()