# но логика та же - придумать типы данных которыми функция подавится
def func(a, b):
    print(set(a) ^ set(b))
    return set(a) ^ set(b)


try:
    func(13, set(['a', '3', 4]))
    print(123 ^ set([range(1, 4)]))
except BaseException:
    print('Ура! Ошибка!')
