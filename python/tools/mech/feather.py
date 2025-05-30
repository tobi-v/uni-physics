from util.uncertainty_calculation import GetResultAndUncertainty

def FeatherConstantOfCoupledPendulum(displacement_left,
                    displacement_right,
                    rod2_l,
                    pendulum2_m,
                    uncertainty=False,
                    delDisplacement_left=0,
                    delDisplacement_right=0,
                    delRod2_l=0,
                    delPendulum2_m=0):
  def FeetherConstantInner(displacement_left, displacement_right, rod2_l, pendulum2_m):
    g = 9.81
    return pendulum2_m*g*(displacement_right) / (rod2_l*(displacement_left - displacement_right))
  
  return GetResultAndUncertainty(FeetherConstantInner,
                                 [displacement_left, displacement_right, rod2_l, pendulum2_m],
                                 uncertainty,
                                 [delDisplacement_left, delDisplacement_right, delRod2_l, delPendulum2_m])