def CheckLengths(*args):
  length = len(args[0])
  for arr in args:
    if len(arr) != length:
      raise ValueError("All input arrays must have the same length.")