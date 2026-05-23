from matplotlib import pyplot as plt
from numpy import abs, pi
from os.path import dirname, join
from pandas import read_csv
from tools.optics.refraction import brewster, simple_refl_p, simple_refl_s, simple_trans_p, simple_trans_s
from tools.statistics.linear_regression import Polyreg
from tools.python.checks import CheckLengths
from tools.python.plot import ScatterWithErrorBars

s_through_mv = 285
p_through_mv = 270

amp_uncertainty = 0.03
angle_uncertainty = 0.5

d = 4e-3
n = 1.515
λ = 532e-9

print(f"Brewster angle: {brewster(1, n)*180/pi:.2f}")

def get_data():
    script_dir = dirname(__file__)
    csv_path = join(script_dir, '22_data.csv')
    data = read_csv(csv_path)
    reflection_data = data[['refl_angle',
                            's_pol_refl_mv',
                            's_refl_dmm_limit',
                            'p_pol_refl_mv',
                            'p_refl_dmm_limit',
                            'p_refl_amp']].dropna()
    transmission_data = data[['trans_angle', 's_pol_trans_mv', 'p_pol_trans_mv']].dropna()

    return reflection_data, transmission_data

def reflection_and_transmission(refl_data, trans_data):
    refl_fig, refl_axs = plt.subplots(2, 1)

    def plot_it(ax, angles, mv, amp, dmm_limit, mv_through, mode, polarity, theoretic_vals, theoretic_uncertainty):
        CheckLengths(theoretic_vals, theoretic_uncertainty)
        mv = mv / amp
        mv_static_uncertainty = dmm_limit/1000.
        mv_relative_uncertainty_dmm = abs(mv*0.005)
        mv_relative_uncertainty_amp = amp*0.03
        mv_uncertainty = mv_static_uncertainty + mv_relative_uncertainty_dmm + mv_relative_uncertainty_amp
        clipped_upper_end = [min(1, x) for x in theoretic_vals+theoretic_uncertainty]
        clipped_lower_end = [max(0, x) for x in theoretic_vals-theoretic_uncertainty]
        ax.plot(angles, clipped_upper_end, label="Theoretische Obergrenze", linestyle='--', color='blue')
        ax.plot(angles, theoretic_vals, label="Theoretisch via Airy", color='blue')
        ax.plot(angles, clipped_lower_end, label="Theoretische Untergrenze", linestyle='--', color='blue')
        ax.fill_between(angles,
                        clipped_lower_end,
                        clipped_upper_end,
                        alpha=0.1,
                        color='blue',
                        label="Unsicherheitsbereich")
        ScatterWithErrorBars(ax, angles, mv/mv_through, angle_uncertainty, mv_uncertainty/mv_through,
                             title=f"{mode} bei {polarity}-Polarisierung",
                             label="Experimentell", xlabel="Einfallswinkel in °", ylabel="Reflexionskoeffizient")
        plt.tight_layout()

    s_pol_refl_theo, Δs_pol_refl_theo = simple_refl_s(refl_data['refl_angle'].to_numpy()*pi/180, n2=n,
                                                      uncertainty=True, Δα=angle_uncertainty*pi/180)
    plot_it(refl_axs[0],
         refl_data['refl_angle'].to_numpy(),
         refl_data['s_pol_refl_mv'].to_numpy(),
         10,
         refl_data['s_refl_dmm_limit'].to_numpy(),
         s_through_mv,
         "Reflexion",
         "s",
         s_pol_refl_theo,
         Δs_pol_refl_theo)
    
    p_pol_refl_theo, Δp_pol_refl_theo = simple_refl_p(refl_data['refl_angle'].to_numpy()*pi/180, n2=n,
                                                      uncertainty=True, Δα=angle_uncertainty*pi/180)
    plot_it(refl_axs[1],
         refl_data['refl_angle'].to_numpy(),
         refl_data['p_pol_refl_mv'].to_numpy(),
         refl_data['p_refl_amp'].to_numpy(),
         refl_data['p_refl_dmm_limit'].to_numpy(),
         p_through_mv,
         "Reflexion",
         "p",
         p_pol_refl_theo,
         Δp_pol_refl_theo)
    
    trans_fig, trans_axs = plt.subplots(2, 1)
    s_pol_trans_theo, Δs_pol_trans_theo = simple_trans_s(trans_data['trans_angle'].to_numpy()*pi/180, n2=n,
                                                      uncertainty=True, Δα=angle_uncertainty*pi/180)
    plot_it(trans_axs[0],
         trans_data['trans_angle'].to_numpy(),
         trans_data['s_pol_trans_mv'].to_numpy(),
         1,
         2,
         s_through_mv,
         "Transmission",
         "s",
         s_pol_trans_theo,
         Δs_pol_trans_theo)
    p_pol_trans_theo, Δp_pol_trans_theo = simple_trans_p(trans_data['trans_angle'].to_numpy()*pi/180, n2=n,
                                                      uncertainty=True, Δα=angle_uncertainty*pi/180)
    plot_it(trans_axs[1],
         trans_data['trans_angle'].to_numpy(),
         trans_data['p_pol_trans_mv'].to_numpy(),
         1,
         2,
         p_through_mv,
         "Transmission",
         "p",
         p_pol_trans_theo,
         Δp_pol_trans_theo)

refl_data, trans_data = get_data()

reflection_and_transmission(refl_data, trans_data)

plt.show()