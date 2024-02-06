numbers = [1, 2, 3, 4, 5]
numbers = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]
print((num for num in numbers if num % 2 != 0))
print(set([num for num in numbers if num % 2 != 0]))
