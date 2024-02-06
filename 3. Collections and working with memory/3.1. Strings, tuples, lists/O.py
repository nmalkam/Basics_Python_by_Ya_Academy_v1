def NOD(first: int, second: int) -> int:
    while first != 0 and second != 0:
        if first > second:
            first = first % second
        else:
            second = second % first
    return first + second


def NOD_2_0() -> int:

    count = 0
    n = int(input())

    if n == 1:
        return int(input())
    res = int(input())
    while count != n - 1:
        number = int(input())
        count += 1
        res = NOD(number, res)
    return res


def NOD_3(list_num: str) -> int:  # 2.4. Nested loops F НОД 2.0

    num = list_num.split(' ')
    # length = len(num)
    res = num[0]

    for _ in num:
        res = NOD(int(_), int(res))
    return res


assert NOD_3('12 42') == 6
assert NOD_3('102 39 768') == 3
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():

    list_num = input()

    print(NOD_3(list_num))


if __name__ == '__main__':
    main()
