from sympy import Matrix, simplify, sqrt, symbols

m1, m2, m3, k = symbols('m1 m2 m3 k')

M = k*Matrix([
    [1/m1,           -1/sqrt(m1*m2), 0],
    [-1/sqrt(m1*m2), 2/m2,           -1/sqrt(m2*m3)],
    [0,              -1/sqrt(m2*m3), 1/m3]
])

eigenvectors = M.eigenvects()
print("=== Eigenvectors ===")
for val, mult, vecs in eigenvectors:
    print(f"\nEigenvalue: {simplify(val)}, Multiplicity: {mult}")
    for vec in vecs:
        print(f"Eigenvector: {simplify(vec)}")