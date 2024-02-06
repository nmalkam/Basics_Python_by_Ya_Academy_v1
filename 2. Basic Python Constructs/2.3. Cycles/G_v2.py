def NOK(first, second):
    n = max(first, second)
    while n % min(first, second) != 0:
        n += max(first, second)
    return n


assert NOK(12, 42) == 84
assert NOK(100, 10) == 100
assert NOK(512, 625) == 320000
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    # first, second = map(int, input().split())
    first = int(input())
    second = int(input())
    print(NOK(first, second))


if __name__ == '__main__':
    main()
# (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31...)
