def func(a, b):
    c = a * b
    return a + b
# Ура! Ошибка!
# def func(a, b):
#     c = a * b
#     return a * b


try:
    func(3.2, '2/2')
except BaseException:
    print('Ура! Ошибка!')

