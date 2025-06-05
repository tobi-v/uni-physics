# Stolen form ct2034

from sympy import Eq, simplify, solve, symbols

given = symbols('u alpha')
u, alpha = given
searched = symbols('u1 u2 u3 u4 u5 u6')
U1, U2, U3, U4, U5, U6 = searched
eqs = [
    # voltage
    Eq(U1 + U2 + U5, u),
    Eq(U2 + U4, U3),
    Eq(U4 + U6, U5),
    Eq(U1 + U3 + U6, u),
    # current
    Eq(U2 + U3, U1),
    Eq(U4 + U5, U2),
    Eq((U3 + U4)/alpha, U6),
    Eq(U5 + U6 * alpha, U1),
]

# 1. Solve for voltages
sol = solve(eqs, searched, dict=True)
simple_sol = {key: simplify(s) for key, s in sol[0].items()}
print(simple_sol)
