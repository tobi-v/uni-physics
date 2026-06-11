from os.path import dirname, join
from pandas import read_csv

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

Ex_32_01_01()