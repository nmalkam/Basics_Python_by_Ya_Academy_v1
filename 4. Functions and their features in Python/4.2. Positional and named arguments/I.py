expression = lambda x: sum(map(int, str(x))) % 2 == 0
print(*filter(expression, (1, 2, 3, 4, 5)))
print(*filter(expression, (32, 64, 128, 256, 512)))

# print(sorted(string.split(), key=lambda line: (len(line), line.lower())))

# result = filter(lambda x: x > 0, [-1, 5, 6, -10, 0])
# print(", ".join(str(x) for x in result))
