from sympy import exp, I, init_printing, simplify, solve, Symbol

# 1a: Reflection

A1 = 1
B1 = Symbol('B1')
A2 = Symbol('A2')
B2 = Symbol('B2')
A3 = Symbol('A3')
k1 = Symbol('k1')
k2 = Symbol('k2')
a = Symbol('a')

EQ1 = A2 + B2 - (1 + B1)
EQ2 = A2*exp(I*k2*a) + B2*exp(-I*k2*a) - A3*exp(I*k1*a)
EQ3 = k2*(A2 - B2) - k1*(1 - B1)
EQ4 = k2*(A2*exp(I*k2*a) - B2*exp(-I*k2*a)) - k1*A3*exp(I*k1*a)

EQ_system = [EQ1, EQ2, EQ3, EQ4]
vars = [B1, A2, B2, A3]

result = solve(EQ_system, vars, dict=True)
init_printing()
print(f"B1: {simplify(result[0][B1])}")