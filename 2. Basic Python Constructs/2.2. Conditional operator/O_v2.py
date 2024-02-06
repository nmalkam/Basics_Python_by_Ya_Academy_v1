n = int(input())
m = int(input())
a = n % 10
b = n // 10 % 10
c = m % 10
d = m // 10 % 10
sr = (a + b + c + d - max(a, b, c, d) - min(a, b, c, d)) % 10
print(f'{max(a, b, c, d)}{sr}{min(a, b, c, d)}')
