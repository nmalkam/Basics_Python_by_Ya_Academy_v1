from itertools import product, islice
print('А Б В')
n = int(input())

for _ in product(range(1, n), repeat=3):
    if sum(_) == n:
        print(*islice(_, 3))
