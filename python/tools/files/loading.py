from inspect import stack
from pandas import read_csv
from os.path import dirname, isabs, join

def load_csv(file, dir=None, delimiter=',', skiprows=0, columns=None):
    """
    Load data from a CSV file and return specified columns as numpy arrays.
    
    Args:
        dir (str, optional): Directory containing the CSV file. If None, uses the caller's directory.
                            If relative, resolves relative to the caller's directory.
                            If absolute, uses the path as-is. Defaults to None.
        columns (list, optional): List of column names to return. If None, returns all columns. Defaults to None.
    
    Returns:
        tuple: Tuple of numpy arrays, one for each specified (or all) column.
    """
    if dir is None: # File to be loaded should be located in the caller script's dir
        dir = dirname(stack()[1].filename)
    elif not isabs(dir): # If dir is relative, resolve it relative to the caller's location
        caller_dir = dirname(stack()[1].filename)
        dir = join(caller_dir, dir)

    csv_path = join(dir, file)
    data = read_csv(csv_path, delimiter=delimiter, skiprows=skiprows)

    if columns is None:
        return tuple(data[col].to_numpy() for col in data.columns)

    return tuple(data[col].to_numpy() for col in columns)