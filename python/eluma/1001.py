import matplotlib.pyplot as plt
from sympy import collect, expand, I, im, latex, re, simplify, symbols

# Ensure LaTeX is used for text rendering
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
})

R, C, L, R_prime, C_prime, omega = symbols("R, C, L, R\', C\', omega", real=True)
Z1, Z2, ZC, Z3, Z4, Z_ges = symbols('Z1, Z2, ZC, Z3, Z4, Z_ges')

ZC = -I/(omega*C_prime)
Z1 = R - I/(omega*C)
Z2 = R_prime + I*omega*C*R**2
Z3 = Z2*ZC/(Z2+ZC)
Z4 = R + Z3
Z_ges = Z1*Z4/(Z1+Z4)

# Split into real and imaginary parts and format
Z_ges_simpl = simplify(Z_ges)
Z_real = simplify(re(Z_ges_simpl))
Z_imag = simplify(im(Z_ges_simpl))
Z_formatted = Z_real + I*Z_imag
latex_expr = latex(Z_formatted, mode='plain')

# Create a figure and render the LaTeX expression
fig, ax = plt.subplots()
ax.text(0.5, 0.5, f'${latex_expr}$', size=20, ha='center', va='center')
ax.set_axis_off()
plt.show()
