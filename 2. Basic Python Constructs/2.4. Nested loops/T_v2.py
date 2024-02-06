def mathematical_benefit(decimal_num) -> int:
    # number systems = системы исчисления (СИСТЕМА ИСЧИСЛЕНИЯ, здесь и далее)

    sum_num = {}
    dict_num_ns = {}
    num_10_to_x = []  # список из десятичной СИ в [2;10] СИ
    copy_decimal_num = decimal_num
    base = 2

    # dict_num_ns[10] = decimal_num
    # sum_num[10] = sum(map(int, str(decimal_num)))
    # dict_num_ns[11] = 11
    # sum_num[11] = 11
    while base != 11:
        while copy_decimal_num >= 1:  # или не 1?
            num_10_to_x.append(int(copy_decimal_num % base))
            copy_decimal_num = int(copy_decimal_num / base)
        copy_decimal_num = int(''.join(map(str, num_10_to_x[::-1])))
        dict_num_ns[base] = copy_decimal_num
        sum_num[base] = sum(map(int, num_10_to_x))
        num_10_to_x = []
        copy_decimal_num = decimal_num
        base += 1

    # minval = max(sum_num.values())
    # res = list(filter(lambda x: sum_num[x] == minval, sum_num))[0]
    # return res
    return max(sum_num, key=sum_num.get)


# assert mathematical_benefit(515) == 7
# assert mathematical_benefit(12) == 7
# assert mathematical_benefit(52) == 9
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():

    num = int(input())

    print(mathematical_benefit(num))


if __name__ == '__main__':
    main()
