def func(a, b, c):
    return ''.join(map(str, (a, b, c)))


class BreakingClass:
    # def __init__(self):
    #     pass

    # def __str__(self):
    #     raise Exception
    #
    def __repr__(self):
        raise Exception


try:
    func(BreakingClass)
except BaseException:
    print('Ура! Ошибка!')
