from numpy import array
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty
from tools.maths.functions import Ratio

def Ex31_leslie():
    ΔT = 0.1
    T = array([86.1, 84.9, 84]) + 273.15
    ΔU_rel = .1
    black = array([.337, .335, .33])   # V
    mirror = array([.1, .1, .099])
    white = array([.335, .33, .325])
    dull = array([.105, .105, .077])

    for b, m, w, d in zip(black, mirror, white, dull):
        pass

def Ex32_r2_dependency():
    d = array([25, 30, 35, 40, 45, 50])*1e-2
    Δd = 0.5e-2
    ΔU_rel = .1
    PT100_1 = 128.9
    U1 = array([1.11, 0.81, 0.635, 0.51, 0.415, 0.35])
    PT100_2 = 129.1
    U2 = array([1.120, .815, .635, .505 ,.415, .345])

def Ex33_coolingBoltzmann():
    pass

def Ex34_pyroBoltzmann():
    pass
