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

    V_mean = array([])
    for m, file in zip(masses, filenames):
        electric_signal = load_data(file)
        V_mean = append(V_mean, electric_signal['Voltage (V)'].mean())

    return Linreg(masses * g, V_mean)


fun, coeff , cov = calibration()
