# 2.4 m Числовой прямоугольник_2

from itertools import product

x = int(input())
y = int(input())

ln = len(str(x * y))

for i, j in product(range(1, x + 1), range(1, y + 1)):
    print(f'{((i - 1) * y + j):>{ln}}', end=' ')
    if j == y:
        print()
