from matplotlib import pyplot as plt
from numpy import abs
from os.path import dirname, join
from pandas import read_csv
from tools.statistics.linear_regression import Polyreg
from tools.python.plot import ScatterWithErrorBars

s_through_mv = 285
p_through_mv = 270

amp_uncertainty = 0.03
# TODO Angle uncertainty?

def get_data():
    script_dir = dirname(__file__)
    csv_path = join(script_dir, '22_data.csv')
    data = read_csv(csv_path)
    calibration_data = data[['cal_angle', 'cal_mv']].dropna()
    reflection_data = data[['refl_angle',
                            's_pol_refl_mv',
                            's_refl_dmm_limit',
                            'p_pol_refl_mv',
                            'p_refl_dmm_limit',
                            'p_refl_amp']].dropna()
    transmission_data = data[['trans_angle', 's_pol_trans_mv', 'p_pol_trans_mv']].dropna()

    return calibration_data, reflection_data, transmission_data

def generate_cal_offset(cal_data):
    cal_amp = 100
    cal_angle = cal_data['cal_angle'].to_numpy()
    cal_mv = cal_data['cal_mv'].to_numpy()/cal_amp
    return Polyreg(cal_angle, cal_mv, 3)

def reflection_and_transmission(refl_data, trans_data, cal_offset):
    refl_fig, refl_axs = plt.subplots(2, 1)

    def plot_it(ax, angle, mv, amp, dmm_limit, mv_through, mode, polarity, cal_offset):
        mv = mv / amp
        mv_static_uncertainty = dmm_limit/1000.
        mv_relative_uncertainty_dmm = abs(mv*0.005)
        mv_relative_uncertainty_amp = amp*0.03
        mv_uncertainty = mv_static_uncertainty + mv_relative_uncertainty_dmm + mv_relative_uncertainty_amp
        ScatterWithErrorBars(ax, angle, (mv-cal_offset(angle))/mv_through, 0, mv_uncertainty/mv_through,
                             title=f"{mode} bei {polarity}-Polarisierung",
                             label="Experimentell", xlabel="Einfallswinkel in °", ylabel="Reflexionskoeffizient")
        plt.tight_layout()
    
    plot_it(refl_axs[0],
         refl_data['refl_angle'].to_numpy(),
         refl_data['s_pol_refl_mv'].to_numpy(),
         10,
         refl_data['s_refl_dmm_limit'].to_numpy(),
         s_through_mv,
         "Reflexion",
         "s",
         cal_offset)    
    plot_it(refl_axs[1],
         refl_data['refl_angle'].to_numpy(),
         refl_data['p_pol_refl_mv'].to_numpy(),
         refl_data['p_refl_amp'].to_numpy(),
         refl_data['p_refl_dmm_limit'].to_numpy(),
         p_through_mv,
         "Reflexion",
         "p",
         cal_offset)
    
    trans_fig, trans_axs = plt.subplots(2, 1)
    plot_it(trans_axs[0],
         trans_data['trans_angle'].to_numpy(),
         trans_data['s_pol_trans_mv'].to_numpy(),
         1,
         2,
         s_through_mv,
         "Transmission",
         "s",
         cal_offset)    
    plot_it(trans_axs[1],
         trans_data['trans_angle'].to_numpy(),
         trans_data['p_pol_trans_mv'].to_numpy(),
         1,
         2,
         p_through_mv,
         "Transmission",
         "p",
         cal_offset)

cal_data, refl_data, trans_data = get_data()
cal_offset, _, _ = generate_cal_offset(cal_data)

reflection_and_transmission(refl_data, trans_data, cal_offset)









plt.show()