# numbers = {1, 2, 3, 4, 5}
numbers = sorted({15, 49, 36})
# {1: [1], 2: [1, 2], 3: [1, 3], 4: [1, 2, 4], 5: [1, 5]}
# {15: [1, 3, 5, 15], 36: [1, 2, 3, 4, 6, 9, 12, 18, 36], 49: [1, 7, 49]}

# d = {}
# for i in numbers:
#     res = []
#     for j in range(1, i + 1):
#         if i % j == 0:
#             res.append(j)
#     d[i] = res[:]
# print(d)

print({i: [j for j in range(1, i + 1) if i % j == 0] for i in numbers})
# print([j for j in range(1, i + 1) if i % j == 0])

# for i, index in enumerate(numbers):
#     res = []
#     for j in range(1, i + 1):
#         if i % j == 0:
#             res.append(j)
