from sympy import exp, I, init_printing, simplify, solve, Symbol

# 1a: Reflection

init_printing()
A1 = 1
B1 = Symbol('B1')
A2 = Symbol('A2')
B2 = Symbol('B2')
A3 = Symbol('A3')
k1 = Symbol('k1')
k2 = Symbol('k2')
k2t = Symbol('k2t')
a = Symbol('a')

EQ1 = A2 + B2 - (1 + B1)
EQ2 = A2*exp(I*k2*a) + B2*exp(-I*k2*a) - A3*exp(I*k1*a)
EQ3 = k2*(A2 - B2) - k1*(1 - B1)
EQ4 = k2*(A2*exp(I*k2*a) - B2*exp(-I*k2*a)) - k1*A3*exp(I*k1*a)

EQ_system1 = [EQ1, EQ2, EQ3, EQ4]
vars = [B1, A2, B2, A3]

result1 = solve(EQ_system1, vars, dict=True)
print(f"B1 for E>V: {simplify(result1[0][B1])}")

EQ5 = A2 + B2 - (1 + B1)
EQ6 = A2*exp(-k2t*a) + B2*exp(k2t*a) - A3*exp(I*k1*a)
EQ7 = k2t*(B2 - A2) - I*k1*(1 - B1)
EQ8 = k2t*(B2*exp(k2t*a) - A2*exp(-k2t*a)) - I*k1*A3*exp(I*k1*a)

EQ_system2 = [EQ5, EQ6, EQ7, EQ8]

result2 = solve(EQ_system2, vars, dict=True)
print(f"B1 for E<V: {simplify(result2[0][B1])}")
