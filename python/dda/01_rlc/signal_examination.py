from matplotlib import pyplot as plt
from os.path import dirname, join
from pandas import read_csv

def load_data(file):
    script_dir = dirname(__file__)
    csv_path = join(script_dir, file)
    data = read_csv(csv_path, delimiter="\t", skiprows=3)
    return data['Time (s)'].to_numpy(), data['Ch.1 (V)'].to_numpy(), data['Ch.2 (V)'].to_numpy()

def plot_signals():
    capacitances = [100, 150, 220]  # [mF]
    frequencies = [500, 1000, 2000] # [Hz]

    fig, axs = plt.subplots(6, 3)

    for ii, C in enumerate(capacitances):
        for jj, f in enumerate(frequencies):
            t, ch1, ch2 = load_data(f'{C}_mf_{f}Hz.csv')
            mask = t <= 10
            t = t[mask]
            ch1 = ch1[mask]
            ch2 = ch2[mask]

            axs[2*ii][jj].plot(t, ch1)
            axs[2*ii][jj].set_xlabel('Zeit [s]')
            axs[2*ii][jj].set_ylabel('Amplitude [V]')
            axs[2*ii][jj].set_title(f'C = {C} mF, f = {f} Hz, Channel 1')
            axs[2*ii+1][jj].plot(t, ch2)
            axs[2*ii+1][jj].set_xlabel('Zeit [s]')
            axs[2*ii+1][jj].set_ylabel('Amplitude [V]')
            axs[2*ii+1][jj].set_title(f'C = {C} mF, f = {f} Hz, Channel 2')

    plt.subplots_adjust(hspace=0.9)
    plt.tight_layout()
    plt.show()

plot_signals()