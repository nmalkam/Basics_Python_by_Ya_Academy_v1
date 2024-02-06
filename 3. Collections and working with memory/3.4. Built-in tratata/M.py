# Расстановка спортсменов
from itertools import permutations, islice

string = []

for _ in range(n := int(input())):
    string.extend(input().split(', '))

for raw in permutations(sorted(string)):
    # print(raw)
    print(', '.join(raw))
