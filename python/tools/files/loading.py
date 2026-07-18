from pandas import read_csv
from os.path import join

def load_csv(dir, file, delimiter=',', skiprows=0):
    csv_path = join(dir, file)
    data = read_csv(csv_path, delimiter=delimiter, skiprows=skiprows)
    return data['Time (s)'].to_numpy(), data['Ch.1 (V)'].to_numpy(), data['Ch.2 (V)'].to_numpy()