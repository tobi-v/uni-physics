from numpy import pi
from util.uncertainty_calculation import GetResultAndUncertainty

def FeetherConstantOfCoupledPendulum(displacement_left,
                    start_right,
                    displacement_right,
                    rod2_l,
                    rod2_m,
                    cylinder2_m,
                    uncertainty=False,
                    delDisplacement_left=0,
                    delStart_right=0,
                    delDisplacement_right=0,
                    delRod2_l=0,
                    delRod2_m=0,
                    delCylinder2_m=0):
  def FeetherConstantInner(displacement_left, start_right, displacement_right, rod2_l, rod2_m, cylinder2_m):
    g = 9.81
    phi1 = start_right / rod2_l
    phi2 = (start_right + displacement_right) / rod2_l
    mass = cylinder2_m + rod2_m
    return mass*g*(phi2 - phi1) / displacement_left
  
  return GetResultAndUncertainty(FeetherConstantInner,
                                 [displacement_left, start_right, displacement_right, rod2_l, rod2_m, cylinder2_m],
                                 uncertainty,
                                 [delDisplacement_left, delStart_right, delDisplacement_right, delRod2_l, delRod2_m, delCylinder2_m])