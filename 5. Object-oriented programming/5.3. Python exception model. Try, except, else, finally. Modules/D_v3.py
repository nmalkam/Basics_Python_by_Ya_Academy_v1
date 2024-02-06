def only_positive_even_sum(a, b):
    # try:
    for _ in [a, b]:
        if _ % 1 != 0 and isinstance(_, int):
            return 'Вызвано исключение TypeError'
        elif _ % 2 == 0 and _ > 0:
            return 'Вызвано исключение ValueError'
    # except TypeError:
    #     return 'Вызвано исключение TypeError'
    # except ValueError:
    #     return 'Вызвано исключение ValueError'
    return a + b


print(only_positive_even_sum("3", 2.5))
# Вызвано исключение TypeError
print(only_positive_even_sum(-5, 4))
# Вызвано исключение ValueError
