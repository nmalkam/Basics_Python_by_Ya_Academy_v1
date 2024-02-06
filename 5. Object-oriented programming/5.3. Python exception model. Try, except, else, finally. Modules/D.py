class NumbersError(Exception):
    pass


class EvenError(NumbersError):
    pass


class NegativeError(NumbersError):
    pass


class IntegerError(NumbersError):
    pass


def only_positive_even_sum(a, b):
    def not_positive_check(num):
        if num > 0:
            return True
        raise ValueError
        # raise NegativeError('Вызвано исключение ValueError')

    def not_even_check(num):
        if num % 2 == 0:
            return True
        raise ValueError
        # raise EvenError('Вызвано исключение ValueError')

    def not_integer(num):
        if num % 1 != 0:
            return False
        if isinstance(num, int):
            return True
        raise TypeError
        # raise IntegerError('Вызвано исключение TypeError')

    try:
        not_integer(a)
        not_integer(b)
        not_positive_check(a)
        not_even_check(a)
        not_positive_check(b)
        not_even_check(b)
    except TypeError:
        return 'Вызвано исключение TypeError'
        # return IntegerError('Вызвано исключение TypeError')
    except ValueError:
        return 'Вызвано исключение ValueError'
    else:
        return a + b


print(only_positive_even_sum("3", 2.5))
# Вызвано исключение TypeError
print(only_positive_even_sum(-5, 4))
# Вызвано исключение ValueError
