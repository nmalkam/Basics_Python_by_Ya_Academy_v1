def zaika5():  # -> (int):  # num: int):
    n = int(input())
    count = 0
    result = 0
    cycle = 0
    while cycle != n:
        word = input()
        if word == 'зайка':
            count += 1
        elif word == 'ВСЁ':
            cycle += 1
            if count != 0:
                result += 1
                count = 0
            if cycle == n:
                return result


def main():
    print(zaika5())


if __name__ == '__main__':
    main()
