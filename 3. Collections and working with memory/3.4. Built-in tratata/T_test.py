# сам тест выглядит очень просто
from random import randint
from T_v5 import truth_tables
from T_SK import m

total = wrong = 0
for _ in range(1000):
    for count in range(1, 201):
        nums = randint(1, 1001)
        total += 1
        if m(nums) != truth_tables(nums):
            wrong += 1
            print(f'Тест номер: {total}, данные: {nums=}, ожидали: {best_base_calc(nums)=}, получили: {mathematical_benefit(nums)=}')  # noqa  # nopep8

print(f'Всего сделано тестов: {total}, ошибок: {wrong}({wrong/total*100:.2f}%)')  # noqa  # nopep8
# A or C ~ not (A -> B) or C
