def recursive_digit_sum(num):
    while num >= 10:
        # print(f'# recursive_digit_sum({num // 10}), {num % 10}')
        return num % 10 + recursive_digit_sum(num // 10)
    return num


# def recursive_digit_sum(num):
#     return num % 10 + recursive_digit_sum(num // 10) if num else 0
# Первый и второй вариант имеют разные граничные условия,
# поэтому первый вариант совершит на один вызов меньше.
