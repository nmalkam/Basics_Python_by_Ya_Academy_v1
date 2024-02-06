# # система НЕ квадратных уравнений
# import numpy as np
#
# # define left-hand side of equation
# left_side = np.array([[4, 2, 1], [3, 5, -2], [2, 2, 4]])
#
# # define right-hand side of equation
# right_side = np.array([0, 0, -9])
#
# # solve for x, y, and z
# np.linalg.inv(left_side).dot(right_side)
#
# # ВЫВОД array([5., 6., 2.])
import sympy
from Q import my_func
# from sympy import solve_all
# система КВАДРАТНЫХ уравнений


a, b, c = sympy.symbols("a b c", real=True)
x1 = -7
x2 = 5
x3 = -1
y1 = y2 = 0
y3 = -9

eq1 = sympy.Eq(a * x1**2 + b * x1 + c, y1)
eq2 = sympy.Eq(a * x2**2 + b * x2 + c, y2)
eq3 = sympy.Eq(a * x3**2 + b * x3 + c, y3)
# sympy.solve([eq1, eq2, eq3])
# assert eq1 == y1
# assert eq2 == y2
# assert eq3 == y3
# a = a.subs({x1: -7, x2: 5, x3: -1})
# print(a)
# b = b.subs({x1: -7, x2: 5, x3: -1})
# c = c.subs({x1: -7, x2: 5, x3: -1})

# my_func(sympy.solve([eq1, eq2, eq3]))
print(sympy.solve([eq1, eq2, eq3]))
# solutions = sympy.solve_all([eq1, eq2, eq3], [a, b, c])
# a = solutions[0][a]
# b = solutions[0][b]
# c = solutions[0][c]
# print(a)
# assert my_func(a, b, c) == 'У! ЗАКОММЕНТИРУЙ СТРОКУ!!'
print('Корни найдены верно. Ура товарищи!')
