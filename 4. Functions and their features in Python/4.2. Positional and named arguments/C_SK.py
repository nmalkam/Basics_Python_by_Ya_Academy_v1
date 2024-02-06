# # типовое решение
#
# def gcd(*args):
#     a = list(args)
#     while len(a) > 1:
#         while a[1]:
#             a[0], a[1] = a[1], a[0] % a[1]
#         a.pop(1)
#     return a[0]


# лаконичное решение

# def gcd(*numbers):
#     a, *tail = numbers
#     for b in tail:
#         while b:
#             a, b = b, a % b
#     return a


assert gcd(3) == 3
