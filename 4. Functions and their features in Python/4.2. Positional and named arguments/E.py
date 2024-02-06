def to_string(*arg, sep=' ', end='\n') -> str:
    lst_elements = []
    for _ in arg:
        lst_elements.append(str(_))
    strng = f'{sep}'.join(lst_elements)
    f'{strng}{end}'
    return f'{strng}{end}'


print(to_string(1, 2, 3))
assert to_string(1, 2, 3) == '1 2 3\n'
data = [7, 3, 1, "hello", (1, 2, 3)]
assert to_string(*data, sep=", ", end="!") == '7, 3, 1, hello, (1, 2, 3)!'
print(to_string(*data, sep=", ", end="!"))
# print(to_string(*data, sep=", ", end="!"), end='0')
print('okay')
