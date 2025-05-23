from sympy import Matrix, simplify, symbols

R1, R2, C1, C2 = symbols("R1 R2 C1 C2")

A = Matrix([[(1/R1 + 1/R2)/C1, 1/R2], [1/(R2*C2), -1/(R2*C2)]])

print(A)

P, D = A.diagonalize()

print(simplify(D))