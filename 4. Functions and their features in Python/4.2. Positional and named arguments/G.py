"""В эфире рубрика «Эксперименты»
В задание не верный Вывод
Не нужно округлять
"""

left = ()
right = ()


def enter_results(*args: float) -> tuple:
    global left, right
    new_left = list(args[::2])
    a = list(args[::])
    a.insert(0, 0)
    new_right = list(a[::2])
    new_right.pop(0)
    left = list(left)
    left.extend(new_left)
    right = list(right)
    right.extend(new_right)
    return right, left


def get_sum() -> tuple:
    sum_left = sum(map(float, left))
    sum_right = sum(map(float, right))
    return sum_left, sum_right


def get_average() -> tuple:
    from statistics import mean
    avg_left = float(mean(left))
    avg_right = float(mean(right))
    return avg_left, avg_right


enter_results(1, 2, 3, 4, 5, 6)
print(get_sum(), get_average())
enter_results(1, 2)
print(get_sum(), get_average())
# (9, 12) (3.0, 4.0)
# (10, 14) (2.5, 3.5)
enter_results(3.5, 2.14, 45.2, 37.99)
print(get_sum(), get_average())
enter_results(5.2, 7.3)
print(get_sum(), get_average())
enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
print(get_sum(), get_average())
# (48.7, 40.13) (24.35, 20.07)
# (53.9, 47.43) (17.97, 15.81)
# (58.27, 54.7) (9.71, 9.12)
