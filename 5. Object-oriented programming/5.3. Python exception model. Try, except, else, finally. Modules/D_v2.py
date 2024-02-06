def only_positive_even_sum(a, b):
    try:
        for _ in [a, b]:
            if _ % 1 != 0 and isinstance(_, int):
                raise TypeError
            elif _ % 2 == 0 and _ > 0:
                raise ValueError
    except TypeError:
        return 'Вызвано исключение TypeError'
    except ValueError:
        return 'Вызвано исключение ValueError'
    else:
        return a + b


print(only_positive_even_sum("3", 2.5))
# Вызвано исключение TypeError
print(only_positive_even_sum(-5, 4))
# Вызвано исключение ValueError
