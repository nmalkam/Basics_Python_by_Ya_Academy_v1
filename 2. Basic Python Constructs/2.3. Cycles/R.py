# наивный способ заключается в том, чтобы каждый раз
# через циклы находить следующее простое число и проверять не делится ли на него наш подопечный.
#
# через решето Эратосфена их сгенерировала и поделила
# def simple_num(num):
#     if num == 1:
#         return "NO"
#     for i in range(2, (num // 2) + 1):
#         if num % i == 0:
#             return "NO"
#     return "YES"


def simple_task_2(num: int) -> str:

    result = ''

    if num == 1:
        print(num)

    q = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 51, 53, 57, 59, 61]
    while num != 1:
        for item in q:
            if num % item == 0:
                num = num / item
                result += str(item) + ' * '
                break
    print(result[:-3])
    return result[:-3]


assert simple_task_2(120) == '2 * 2 * 2 * 3 * 5'
assert simple_task_2(98) == '2 * 7 * 7'
# assert simple_task_2(1111198) == '2 * 7 * 7'
assert simple_task_2(1118) == '2 * 13 * 43'
print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    num = int(input())
    print(simple_task_2(num))


if __name__ == '__main__':
    main()
    # count = 0
    # res = ''
    #
    # while count != num:
