# не вспомнил как записать несколько значений для функции replace
def make_linear(iterable: list):
    # return list([int(letter) for letter in str(iterable) if letter not in "[], "])
    strng = str(iterable).replace("["  "]", '')
    print()

result = make_linear([1, 2, [3]])
print(result)
result = make_linear([1, [2, [3, 4]], 5, 6])
print(result)
# [1, 2, 3, 4, 5, 6]
