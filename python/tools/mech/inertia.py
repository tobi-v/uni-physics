from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

def Rod(mass, length, uncertainty=False, delM=0, delL=0):
  def RodInner(mass, length):
    return (mass*length**2)/3
  
  return GetResultAndUncertainty(RodInner, [mass, length], uncertainty, [delM, delL])

def HollowCylinder(m, r1, r2, uncertainty=False, delM=0, delR1=0, delR2=0):
  def HollowCylinderInner(m, r1, r2):
    return 0.5*m*(r1**2 + r2**2)
    
  return GetResultAndUncertainty(HollowCylinderInner,
                                 [m, r1, r2],
                                 uncertainty, [delM, delR1, delR2])

def CylinderXY(mass, length, r, uncertainty=False, delM=0, delL=0, delR=0):
  def CylinderXYInner(mass, length, r):
    return mass*((r**2)/4 + (length**2)/12)
  
  return GetResultAndUncertainty(CylinderXYInner,
                                 [mass, length, r],
                                 uncertainty, [delM, delL, delR])

def Steiner(inertia, m, displacement, uncertainty=False, delI=0, delM=0, delDispl=0):
  def SteinerInner(inertia, m, displacement):
    return inertia + m*displacement**2

  return GetResultAndUncertainty(SteinerInner,
                                 [inertia, m, displacement],
                                 uncertainty, [delI, delM, delDispl])