from random import randint, choice
from T import polish_calculator_2
from T_SK import my_func_pol

total = wrong = 0
for _ in range(1000):
    for count in range(1, 201):
        expression = ''
        for num in range(5):
            expression += str(randint(1, 1001)) + ' '
        for sign in range(1):
            expression += choice('@#!') + ' '
        for sign in range(4):
            expression += choice('+-*~') + ' '
        total += 1
        print(expression)
        if my_func_pol(expression) != polish_calculator_2(expression):
            wrong += 1
            print(f'Тест номер: {total}, данные: {expression=},'
                  f' ожидали: {my_func_pol(expression)=},'
                  f' получили: {polish_calculator_2(expression)=}')
            # noqa  # nopep8

print(f'Всего сделано тестов: {total},'
      f' ошибок: {wrong}({wrong/total*100:.2f}%)')  # noqa  # nopep8
