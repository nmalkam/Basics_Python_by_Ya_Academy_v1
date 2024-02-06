# сам тест выглядит очень просто
from random import randint
from T_v2 import mathematical_benefit
from T_SK import best_base_calc

total = wrong = 0
for _ in range(1000):
    for count in range(1, 201):
        nums = randint(1, 1001)
        total += 1
        if best_base_calc(nums) != mathematical_benefit(nums):
            wrong += 1
            print(f'Тест номер: {total}, данные: {nums=}, ожидали: {best_base_calc(nums)=}, получили: {mathematical_benefit(nums)=}')  # noqa  # nopep8

print(f'Всего сделано тестов: {total}, ошибок: {wrong}({wrong/total*100:.2f}%)')  # noqa  # nopep8
