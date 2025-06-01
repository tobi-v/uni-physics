from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

def FeatherConstantOfCoupledPendulum(displ_left,
                    displ_right,
                    rod2_l,
                    pendulum2_m,
                    uncertainty=False,
                    delDispl_left=0,
                    delDispl_right=0,
                    delRod2_l=0,
                    delPendulum2_m=0):
  '''
  displ_left: displacement of the left pendulum
  displ_right: displacement of the right pendulum
  
  Returns: Feather constant'''
  def FeetherConstantInner(displ_left, displ_right, rod2_l, pendulum2_m):
    g = 9.81
    return pendulum2_m*g*(displ_right) / (rod2_l*(displ_left - displ_right))
  
  return GetResultAndUncertainty(FeetherConstantInner,
                                 [displ_left, displ_right, rod2_l, pendulum2_m],
                                 uncertainty,
                                 [delDispl_left,
                                  delDispl_right,
                                  delRod2_l,
                                  delPendulum2_m])