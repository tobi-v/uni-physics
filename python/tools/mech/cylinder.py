from numpy import pi
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

def VolumeOfCylinder(length, radius, uncertainty=False, delL=0, delR=0):
    def VolumeOfCylinderInner(length, radius):
        return pi * length * radius**2

    return GetResultAndUncertainty(
        VolumeOfCylinderInner, [length, radius], uncertainty, [delL, delR]
    )

def MassFromVolume(length, radius, rho, uncertainty=False, delL=0, delR=0, delRho=0):
    def MassFromVolumeInner(length, radius, rho):
        return rho * pi * length * radius**2

    return GetResultAndUncertainty(
        MassFromVolumeInner, [length, radius, rho], uncertainty, [delL, delR, delRho]
    )
