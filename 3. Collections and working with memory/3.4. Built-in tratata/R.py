from itertools import product
string = input()
print('a b c f')
for a, b, c in product(range(2), repeat=3):
    print(a, b, c, int(eval(string, {'a': a, 'b': b, 'c': c})))
    # print(a, b, c, int(eval(string)))
