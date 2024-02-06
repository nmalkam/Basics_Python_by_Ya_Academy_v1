# numbers = [3, 1, 2, 3, 2, 2, 1]
numbers = [1, 1, 3, 1, 10, 2, 4, 6, 7, 1, 2, 7]
# '1 - 2 - 3'
# '1 - 2 - 3 - 4 - 6 - 7 - 10'
' - '.join(map(str, set(numbers)))
print(' - '.join(map(str, sorted(set(numbers)))))



# d = {char: text.lower().count(char) for char in set(text.lower()) if char.isalpha()}
