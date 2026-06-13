from tools.maths.functions import norm2D, product

# TODO: Make flexible n-dimensional
def impulse1D(m, v, uncertainty=False, Δm=0, Δv=0):
    return product(m, v, uncertainty, Δm, Δv)

def impulse2D(m, v_x, v_y, uncertainty=False, Δm=0, Δv_x=0, Δv_y=0):
    p_x = product(m, v_x, uncertainty, Δm, Δv_x)
    p_y = product(m, v_y, uncertainty, Δm, Δv_y)

    if uncertainty:
        return zip(p_x[0], p_y[0]), zip(p_x[1], p_y[1])
    else:
        return p_x, p_y

def total_impulse2D(p_x, p_y, uncertainty=False, Δp_x=0, Δp_y=0):
    return norm2D(p_x, p_y, uncertainty, Δp_x, Δp_y)