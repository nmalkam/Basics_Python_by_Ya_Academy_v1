def NOD(first, second):
    while first != 0 and second != 0:
        if first > second:
            first = first % second
        else:
            second = second % first
    return second + first


assert NOD(12, 42) == 6
assert NOD(512, 625) == 1
# print("Успешно! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    # t_room, t_cond = map(int, input().split())
    first = int(input())
    second = int(input())
    print(NOD(first, second))


if __name__ == '__main__':
    main()
