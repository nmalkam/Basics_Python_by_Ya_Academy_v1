def only_positive_even_sum(a, b):
    if not isinstance(a, int) and not isinstance(b, int):
        raise TypeError
    elif a % 1 != 0 or b % 1 != 0:
        raise TypeError
    elif a % 2 == 0 or a < 0:
        raise ValueError
    elif b % 2 == 0 or b < 0:
        raise ValueError
    else:
        return a + b


print(only_positive_even_sum("3", 2.5))
# Вызвано исключение TypeError
print(only_positive_even_sum(-5, 4))
# Вызвано исключение ValueError
