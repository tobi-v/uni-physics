from util.uncertainty_calculation import GetResultAndUncertainty

def Rod(m, l, uncertainty=False, delM=0, delL=0):
  def RodInner(m, l):
    return (m*l**2)/3
  
  return GetResultAndUncertainty(RodInner, [m, l], uncertainty, [delM, delL])

def HollowCylinder(m, r1, r2, uncertainty=False, delM=0, delR1=0, delR2=0):
  def HollowCylinderInner(m, r1, r2):
    return 0.5*m*(r1**2 + r2**2)
    
  return GetResultAndUncertainty(HollowCylinderInner, [m, r1, r2], uncertainty, [delM, delR1, delR2])

def CylinderXY(m, l, r, uncertainty=False, delM=0, delL=0, delR=0):
  def CylinderXYInner(m, l, r):
    return m*((r**2)/4 + (l**2)/12)
  
  return GetResultAndUncertainty(CylinderXYInner, [m, l, r], uncertainty, [delM, delL, delR])

def Steiner(inertia, m, displacement, uncertainty=False, delI=0, delM=0, delDispl=0):
  def SteinerInner(inertia, m, displacement):
    return inertia + m*displacement**2

  return GetResultAndUncertainty(SteinerInner, [inertia, m, displacement], uncertainty, [delI, delM, delDispl])