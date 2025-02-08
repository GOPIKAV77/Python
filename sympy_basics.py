
import sympy

a = sympy.Symbol('a')
expression_1 = a**2+a**3+3*a**2
print(expression_1)

#To find the arguments in the expression_1

print(expression_1.args)

print(expression_1.args[0])
print(expression_1.args[1])

#for simplifying an expression

#use sympy.simplify

expression_2 = a**2+3*a+4*a**2+a*(a+1)-2*a
print(sympy.simplify(expression_2))

expression_3 = sympy.cos(a)+sympy.sin(a)
print(sympy.simplify(expression_3))

#expand an equation

expression_4 = (a**2+a+2)*(3*a+1)
print(sympy.expand(expression_4))

#to factorize an equation

expression_5 = 3*a**3 + 4*a**2 + 7*a + 2
print(sympy.factor(3*a**3 + 4*a**2 + 7*a + 2))

#To collect terms

b = sympy.Symbol("b")
c = sympy.Symbol("c")

expression_6 = a*b + b*c + a*c + a*b*c + a + b + c
print(expression_6.collect(c))

#To substitute
expression_7 = a*b + b**2 + a + b
print(expression_7.subs({a:1,b:2}))
