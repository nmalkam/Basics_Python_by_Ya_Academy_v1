numbers = [1, 2, 3, 4, 5]
numbers = [number for number in range(16, 100, 4)]
print((num for num in numbers if num % (num ** 0.5) == 0))
print(set([num for num in numbers if num % (num ** 0.5) == 0]))
