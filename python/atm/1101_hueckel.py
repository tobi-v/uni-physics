from sympy import Matrix, symbols

α, β = symbols('α β')

def eigen_fun(m: Matrix):
    eigenvectors = M1.eigenvects()
    print("=== Eigenvectors ===")
    for val, mult, vecs in eigenvectors:
        print(f"\nEigenvalue: {val}, Multiplicity: {mult}")
        for vec in vecs:
            print(f"Eigenvector: {vec}")


M1 = Matrix([
    [α, β, 0, β],
    [β, α, β, 0],
    [0, β, α, β],
    [β, 0, β, α]
])

M2 = Matrix([
    [α, β, 0, 0, 0, β],
    [β, α, β, 0, 0, 0],
    [0, β, α, β, 0, 0],
    [0, 0, β, α, β, 0],
    [0, 0, 0, β, α, β],
    [β, 0, 0, 0, β, α]
])

eigen_fun(M2)#
