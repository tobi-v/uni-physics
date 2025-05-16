from util.uncertainty_calculation import GetResultAndUncertainty

c_W = 4200 # [J/(kg*K)]
c_Ice = 2060 # [J/(kg*K)]

def WaterEquivalent(T_H, T_K, T_M, m_H, m_K, uncertainty=False, delT=0, delM=0):
  def WaterEquivaletInner(T_H, T_K, T_M, m_H, m_K):
    return c_W * (m_H *(T_H - T_M)/(T_M-T_K) - m_K)
  
  return GetResultAndUncertainty(WaterEquivaletInner,
                                 [T_H, T_K, T_M, m_H, m_K],
                                 uncertainty,
                                 [delT, delT, delT, delM, delM])

def SpecificHeat(T_H, T_K, T_M, m_W, m_K, C_D, uncertainty=False, delT=0, delM=0, delC_D=0):
  def SpecificHeatInner(T1, T2, T_M, m_W, M_K, C_D):
    return (m_W*c_W + C_D)*(T_M - T1)/(M_K *(T2 - T_M))
  
  return GetResultAndUncertainty(SpecificHeatInner,
                                 [T_H, T_K, T_M, m_W, m_K, C_D],
                                 uncertainty,
                                 [delT, delT, delT, delM, delM, delC_D])



def CMeltIce(T_H, T_M, m_W, m_Ice, C_D, uncertainty=False, delT=0, delM=0, delC_D=0):
  def CMeltIceInner(T_H, T_M, m_W, m_Ice, C_D):
    T_melt = 273.15
    return (m_W*c_W + C_D)*(T_H - T_M)/m_Ice - c_W*(T_M - T_melt)# - c_Ice*(T_melt - T_K)
  
  return GetResultAndUncertainty(CMeltIceInner,
                                 [T_H, T_M, m_W, m_Ice, C_D],
                                 uncertainty,
                                 [delT, delT, delM, delM, delC_D])

def CSteamCondensation(T_K, T_M, m_W, m_D, C_D, uncertainty=False, delT=0, delM=0, delC_D=0):
  def CSteamCondensationInner(T_K, T_M, m_W, m_D, C_D):
    T_boil = 283.15
    return (m_W*c_W + C_D)*(T_M-T_K)/m_D - c_W*(T_boil-T_M)
  
  return GetResultAndUncertainty(CSteamCondensationInner,
                                 [T_K, T_M, m_W, m_D, C_D],
                                 uncertainty,
                                 [delT, delT, delM, delM, delC_D])

def CSteamCondensationElectric(U, I, t, m_D, uncertainty=False, delU=0, delI=0, delt=0, delM=0):
  def CSteamCondensationElectricInner(U, I, t, m_D):
    T_boil = 283.15
    return U*I*t/m_D
  
  return GetResultAndUncertainty(CSteamCondensationElectricInner,
                                 [U, I, t, m_D],
                                 uncertainty,
                                 [delU, delI, delt, delM])