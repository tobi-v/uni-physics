# Stolen form ct2034

from sympy import Eq, simplify, solve, symbols

given = symbols('U alpha')
U, alpha = given
searched = symbols('U1 U2 U3 U4 U5 U6')
U1, U2, U3, U4, U5, U6 = searched
eqs = [
    # voltage
    Eq(U1 + U2 + U5, U),
    Eq(U2 + U4, U3),
    Eq(U4 + U6, U5),
    Eq(U1 + U3 + U6, U),
    # current
    Eq(U2 + U3, U1),
    Eq(U4 + U5, U2),
    Eq((U3 + U4)/alpha, U6),
    Eq(U5 + U6 * alpha, U1),
]

# 1. Solve for voltages
sol = solve(eqs, searched, dict=True)
simple_sol = {key: simplify(s) for key, s in sol[0].items()}
print(f"\nVolagtes: {simple_sol}")

# 2. Find equivalent resistance
R1, equi_R = symbols('R1, equi_R')
equi_R = simplify(R1 * U / simple_sol[U1])
print(f"\nEquivalent resistance: {equi_R}\n")
