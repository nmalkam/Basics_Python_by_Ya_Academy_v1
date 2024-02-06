from itertools import product

expression = input()

variables = [x for x in sorted(set(expression.split())) if x.isupper()]
length = len(variables)

print(*[v for v in variables], 'F')

for value in product([0, 1], repeat=length):
    d = {key: value for key, value in zip(variables, value)}
    print(*[v for v in d.values()], int(eval(expression, d)))
