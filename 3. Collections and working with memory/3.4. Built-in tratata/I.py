from itertools import product, islice

# print(list(product(range(1, 3 + 1), repeat=2)))
# print(list(range(1, 3 + 1)))
# print(range(1, 3 + 1))


size = 3  # int(input())

nums = range(1, size + 1)

table = [x * y for x, y in product(nums, repeat=2)]

for row in range(size):
    print(*islice(table, row * size, (row + 1) * size))
# print(*islice(table, 0 * 3, (0 + 1) * 3))
