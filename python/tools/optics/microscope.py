from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

def magnification(d, f_Oku, f_Obj, s_0, uncertainty=False, Δd = 0, Δf_Oku = 0, Δf_Obj = 0, Δs_0 = 0):
    def magnification_inner(d, f_Oku, f_Obj, s_0):
        return (d - f_Obj)*s_0/(f_Oku*f_Obj)
    
    return GetResultAndUncertainty(magnification_inner, [d, f_Oku, f_Obj, s_0], uncertainty, [Δd, Δf_Oku, Δf_Obj, Δs_0])

def magnification_obj(d, f_Obj, uncertainty=False, Δd = 0, Δf_Obj = 0):
    def magnification_inner(d, f_Obj):
        return (d - f_Obj)/f_Obj
    
    return GetResultAndUncertainty(magnification_inner, [d, f_Obj], uncertainty, [Δd, Δf_Obj])
    