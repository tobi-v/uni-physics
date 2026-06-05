from os.path import dirname, join
from pandas import read_csv

def read(file):
    script_dir = dirname(__file__)
    csv_path = join(script_dir, file)
    data = read_csv(csv_path)
    return data