from math import pi
from numpy import allclose
from tools.maths.angles import dms_to_rad

def test_180_to_pi():
    assert allclose(dms_to_rad(180.0), pi), "Gaussian should reach its peak at the mean"


def test_30_minutes_to_correct_value():
    assert allclose(dms_to_rad(0.3), 0.5*pi/180.0), "Gaussian should reach its peak at the mean"