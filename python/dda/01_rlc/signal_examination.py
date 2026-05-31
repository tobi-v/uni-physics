from matplotlib import pyplot as plt
from os.path import dirname, join
from pandas import read_csv
from tools.signals.fourier import fft

def load_data(file):
    script_dir = dirname(__file__)
    csv_path = join(script_dir, file)
    data = read_csv(csv_path, delimiter="\t", skiprows=3)
    return data['Time (s)'].to_numpy(), data['Ch.1 (V)'].to_numpy(), data['Ch.2 (V)'].to_numpy()

def plot_signals():
    capacitances = [100, 150, 220]  # [mF]
    frequencies = [500, 1000, 2000] # [Hz]

    _, t_axs = plt.subplots(6, 3)
    _, ft_axs = plt.subplots(6,3)

    def plot(ax, channel, C, f, x, y, x_label):
        ax.plot(x, y)
        ax.set_xlabel(x_label)
        ax.set_ylabel('Amplitude [V]')
        ax.set_title(f'C = {C} mF, f = {f} Hz, Channel {channel}')

    for ii, C in enumerate(capacitances):
        for jj, f in enumerate(frequencies):
            t, ch1, ch2 = load_data(f'{C}_mf_{f}Hz.csv')
            mask = t <= 10
            t = t[mask]
            ch1 = ch1[mask]
            ch2 = ch2[mask]

            plot(t_axs[2*ii][jj], 1, C, f, t, ch1, x_label="Zeit [s]")
            plot(t_axs[2*ii+1][jj], 2, C, f, t, ch2, x_label="Zeit [s]")
            plt.subplots_adjust(hspace=0.9)

            _, ch1_ft = fft(t, ch1)
            freqs, ch2_ft = fft(t, ch2)
            
            plot(ft_axs[2*ii][jj], 1, C, f, freqs, ch1_ft, x_label="Frequenz [s]")
            plot(ft_axs[2*ii+1][jj], 2, C, f, freqs, ch2_ft, x_label="Frequenz [s]")
            plt.subplots_adjust(hspace=0.9)

plot_signals()
plt.show()