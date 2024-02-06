def fibonacci(num: int):
    f, s = 0, 1
    for step in range(num):
        yield f
        r = f + s
        f = s
        s = r
        # f, s = s, f + s


print(*fibonacci(5))
print(*fibonacci(10), sep=', ')
