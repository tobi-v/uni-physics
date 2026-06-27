from numpy import append, array
from os.path import dirname, join
from pandas import read_csv
from tools.statistics.linear_regression import Linreg

g = 9.81

def load_data(file):
    script_dir = dirname(__file__)
    csv_path = join(script_dir, file)
    return read_csv(csv_path, delimiter="\t", skiprows=3)

def calibration():
    masses = array([0, 0.5, 1.0, 2.0])
    filenames = ['Kalibrierung-0.csv', 'Kalibrierung-0_5.csv', 'Kalibrierung-1_0.csv', 'Kalibrierung-2_0.csv']

    V_means = array([])
    V_stds = array([])
    for m, file in zip(masses, filenames):
        electric_signal = load_data(file)
        V_mean = electric_signal['Voltage (V)'].mean()
        V_std = electric_signal['Voltage (V)'].std()

        print(f"Masse m={m} kg, Spannung U={V_mean:.4f} pm {V_std:.4f}")

        V_means = append(V_means, V_mean)
        V_stds = append(V_stds, V_std)


    print(f"Die Mittelwerte für die Spannung zu den Massen {masses} sind {V_means}.")

    fun, coeff, cov = Linreg(masses * g, V_means)
    print(f"Die Kennlinie des Messgerätes für Kraft auf Spannung ist {fun}")

    return fun, coeff, cov

fun, coeff, cov = calibration()