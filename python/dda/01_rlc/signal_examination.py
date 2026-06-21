from matplotlib import pyplot as plt
from numpy import argmax, max, mean, ones_like, pi, var
from os.path import dirname, join
from pandas import read_csv
from tools.electricity.RLC_circuit import SeriesAmplitudeAtR
from tools.signals.fourier import fft

def load_data(file):
    script_dir = dirname(__file__)
    csv_path = join(script_dir, file)
    data = read_csv(csv_path, delimiter="\t", skiprows=3)
    return data['Time (s)'].to_numpy(), data['Ch.1 (V)'].to_numpy(), data['Ch.2 (V)'].to_numpy()

def plot_signals():
    capacitances = [100, 150, 220]  # [μF]
    frequencies = [500, 1000, 2000] # [Hz]
    resistors = 10 # [Ohm]
    L = 15e-3 # [H]
    R = resistors/2 + 0.12

    t_fig, t_axs = plt.subplots(6, 3)
    plt.subplots_adjust(hspace=0.9)
    ft_fig, ft_axs = plt.subplots(6,3)
    plt.subplots_adjust(hspace=0.9)

    def plot(ax, channel, C, f, x, y, x_label, label="Messwerte"):
        ax.plot(x, y, label=label)
        ax.set_xlabel(x_label)
        ax.set_ylabel('Amplitude [V]')
        ax.set_title(f'C = {C} μF, f = {f} Hz, Channel {channel}')
        
    bounds_100muF = [[1.7, 11.5], [6.6, 16.4], [8.9, 18.7]]
    bounds_150muF = [[8.4, 18.1], [8.6, 18.3], [2.6, 12.3]]
    bounds_220muF = [[14.0, 23.5], [5.4, 15.1], [3.9, 13.7]]
    bounds = [bounds_100muF, bounds_150muF, bounds_220muF]

    for ii, C in enumerate(capacitances):
        max_fs = []
        for jj, f in enumerate(frequencies):
            t, ch1, ch2 = load_data(f'{C}_mf_{f}Hz.csv')
            t_mask = (t >= bounds[ii][jj][0]) & (t <= bounds[ii][jj][1])
            t = t[t_mask]
            ch1 = ch1[t_mask]
            ch2 = ch2[t_mask]

            plot(t_axs[2*ii][jj], 1, C, f, t, ch1, x_label="Zeit [s]")
            plot(t_axs[2*ii+1][jj], 2, C, f, t, ch2, x_label="Zeit [s]")
            
            freqs, ch1_ft = fft(t, ch1)
            max_f = freqs[argmax(ch1_ft)]
            max_fs.append(max_f)
            _, ch2_ft = fft(t, ch2)

            f_mask = freqs < 300
            freqs = freqs[f_mask]
            ch1_ft = ch1_ft[f_mask]
            ch2_ft = ch2_ft[f_mask]

            theo = SeriesAmplitudeAtR(freqs*2*pi, R*ones_like(freqs), L*ones_like(freqs), C*1e-6*ones_like(freqs))
            theo_max_f = freqs[argmax(theo)]
            
            plot(ft_axs[2*ii][jj], 1, C, f, freqs, ch1_ft/max(ch1_ft), x_label="Frequenz [Hz]")
            ft_axs[2*ii][jj].axvline(max_f, color='b', linestyle='--', label=f"Maximum bei {max_f:.1f} Hz")
            ft_axs[2*ii][jj].plot(freqs, theo, "k-", label="Theoriekurve")
            ft_axs[2*ii][jj].axvline(theo_max_f, color='k', linestyle='--', label=f"Maximum bei {theo_max_f:.1f} Hz")
            ft_axs[2*ii][jj].legend(loc='right')
            plot(ft_axs[2*ii+1][jj], 2, C, f, freqs, ch2_ft, x_label="Frequenz [Hz]")

        print(f"Maximum frequency for C = {C}: f = {mean(max_fs):.2f} ± {var(max_fs):.2f}")

    # plt.close(t_fig)
    # plt.close(ft_fig)

plot_signals()
plt.show()