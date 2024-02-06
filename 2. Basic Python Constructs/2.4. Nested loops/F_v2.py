def NOD(first, second):
    while first != 0 and second != 0:
        if first > second:
            first = first % second
        else:
            second = second % first
    return first + second


def NOD_2_0():
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


def main():
    print(NOD_2_0())


if __name__ == '__main__':
    main()
