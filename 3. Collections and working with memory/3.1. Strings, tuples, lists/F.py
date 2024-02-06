def zaika6() -> int:

    res = 0
    count = 0

    n = int(input())
    while count != n:
        string = input()
        words_list = string.split(' ')
        for word in words_list:
            if 'зайка' in word:
                res += 1
        count += 1
    return res


def main():
    print(zaika6())


if __name__ == '__main__':
    main()
