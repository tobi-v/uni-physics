from sympy import Matrix, symbols

α, β = symbols('α β')

M = Matrix([
    [α, β, 0, β],
    [β, α, β, 0],
    [0, β, α, β],
    [β, 0, β, α]
])

eigenvectors = M.eigenvects()
print("=== Eigenvectors ===")
for val, mult, vecs in eigenvectors:
    print(f"\nEigenvalue: {val}, Multiplicity: {mult}")
    for vec in vecs:
        print(f"Eigenvector: {vec}")