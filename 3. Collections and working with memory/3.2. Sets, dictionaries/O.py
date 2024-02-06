def binary_statistics(s):

    lst_decimal = list(map(int, s.split()))  # [44]  #
    lst_binary = []
    res = []

    for num in lst_decimal:
        reminder = ''
        while num > 0:
            reminder += str(num % 2)
            num = num // 2
        lst_binary.append(reminder[::-1])

    for n in lst_binary:
        d = {"digits": len(n), "units": 0, "zeros": 0}
        for digit in n:
            if digit == '1':
                d['units'] = d.get('units') + 1
            if digit == '0':
                d['zeros'] = d.get('zeros') + 1
        res.append(d)
    print(res)


# assert binary_statistics('13 2 7') == 1
# assert binary_statistics('5 8 12') == 1
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():

    s = input()

    binary_statistics(s)


if __name__ == '__main__':
    main()
