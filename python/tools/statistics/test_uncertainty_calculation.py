from numpy import array

from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

single_value_single_point   = 7
single_value_multi_point    = array([[3], [5], [-3]])
multi_value_single_point    = array([3, 5, -3])
multi_value_multi_point     = array([[3, 5, -3],
                                     [4, 6, -4],
                                     [5, 7, -5],
                                     [6, 8, -6],
                                     [7, 9, -7]])

def SingleValueFunc(param: float):
    return 10*param + 5

def MultiValueFunc(param1: float, param2: float, param3: float):
    return param1*param2/param3

def test_GetResult_single_value_single_point():
    result = GetResultAndUncertainty(SingleValueFunc, single_value_single_point)
    assert result == 75

def test_GetResult_single_value_multi_point():
    pass

def test_GetResult_multi_value_single_point():
    pass

def test_GetResult_multi_value_multi_point():
    pass
