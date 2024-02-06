from itertools import permutations, islice

names = []

for _ in range(num := int(input())):
    names.extend(input().split(', '))

names.sort()

for name in permutations(names, 3):
    print(*islice(name, 10))
