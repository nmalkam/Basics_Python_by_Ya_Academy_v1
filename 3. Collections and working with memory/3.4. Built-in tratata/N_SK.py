from itertools import permutations
names = []

for _ in range(num := int(input())):
    names.extend(input().split())

names.sort()

for name_list in permutations(names, 3):
    print(', '.join(name_list))
