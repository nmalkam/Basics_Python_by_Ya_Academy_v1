# res = [0]
# a, b = map(int, [[int(num) for num in input().split() if num.isdigit()] for _ in range(2)])
# if a[0] < 0:
#     res.append([num ** 2 for num in range(abs(a[0]), b[0] + 1)][::-1])
a = -5
b = 5
[num ** 2 for num in range(a, b + 1)]
# print(res)
# print()
