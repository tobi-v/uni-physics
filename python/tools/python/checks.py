def CheckLengths(*args):
  lengths = []
  for arg in args:
    if hasattr(arg, '__len__'):
      lengths.append(len(arg))
    else:
      lengths.append(1)
  
  if lengths and not all(l == lengths[0] for l in lengths):
    raise ValueError("All input arrays must have the same length.")
