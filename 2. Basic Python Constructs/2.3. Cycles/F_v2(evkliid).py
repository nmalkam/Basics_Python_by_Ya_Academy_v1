def NOD(first, second):  # наибольший общий делитель (НОД)
    if first > second:
        bigger = first
        smaller = second
    else:
        bigger = second
        smaller = first
    remainder = 0
    while bigger % smaller != 0:
        remainder = bigger % smaller
        bigger = smaller
        smaller = remainder
    return remainder


assert NOD(12, 42) == 6
assert NOD(512, 625) == 1
# assert NOD(51200000000, 6200000000005) == 1
print("Успешно! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    first = int(input())
    second = int(input())
    # t_room, t_cond = map(int, input().split())
    print(NOD(first, second))


if __name__ == '__main__':
    main()
