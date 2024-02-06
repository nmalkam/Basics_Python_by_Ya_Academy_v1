# сам тест выглядит очень просто
from random import uniform
from G import enter_results, get_sum, get_average
from G_SK import enter_results_, get_sum_, get_average_

total = wrong = 0
for _ in range(1000):
    for count in range(1, 201):
        r_list = [uniform(1, 1001) for _ in range(10)]
        total += 1
        enter_results(*r_list)
        enter_results_(*r_list)
        # print(r_list)
        # print(get_sum_())
        # print(get_sum())
        # print()
        # print(get_average_())
        # print(get_average())
        if get_sum_() != get_sum():
            wrong += 1
            print(f'Тест номер: {total}, данные: {r_list},\n\n ожидали: \n\n{get_sum_()}, \nполучили: \n\n{get_sum_()}')  # noqa  # nopep8
        if get_average_() != get_average():
            wrong += 1
            print(f'Тест номер: {total}, данные: {r_list},\n\n ожидали: \n\n{get_average_()}, \n\nполучили: \n\n{get_average()}')  # noqa  # nopep8

print(f'Всего сделано тестов: {total}, ошибок: {wrong}({wrong/total*100:.2f}%)')  # noqa  # nopep8
