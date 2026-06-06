from matplotlib import pyplot as plt
from os.path import dirname, join
from pandas import read_csv
from tools.statistics.linear_regression import PlotLinregWithErrorAndScatterErrorbars
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

Δs = 0.1 # [cm]

def read(file):
    script_dir = dirname(__file__)
    csv_path = join(script_dir, file)
    data = read_csv(csv_path)
    return data

def λ_from_maxima(s_u, s_o, n):
    def λ_from_maximaInner(s_u, s_o, n):
        return (s_o - s_u) / (2*n)
    
    return GetResultAndUncertainty(λ_from_maximaInner, [s_u, s_o, n], uncertainty=True, uncertainty_params=[Δs, Δs, 0])

def sound_in_gases(file):
    data = read(join('09_data', file))
    freqs = data['f'].to_numpy()
    s_u = data['s_u'].to_numpy()
    s_o = data['s_o'].to_numpy()
    n = data['n'].to_numpy()

    λ, Δλ = λ_from_maxima(s_u, s_o, n)
    print(f'{λ}\n {Δλ}')

sound_in_gases('air_data.csv')
sound_in_gases('co2_data.csv')