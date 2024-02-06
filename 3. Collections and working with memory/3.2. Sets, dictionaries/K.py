def namesakes():

    res = 0
    d = {}

    for _ in range(int(input())):
        surname = input()
        d[surname] = d.get(surname, 0) + 1

    for key, val in set(d.items()):
        if val > 1:
            res += val

    # print(res)
    return res


# assert namesakes(748) == "NO"
# assert namesakes(123) == "YES"
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    print(namesakes())


if __name__ == '__main__':
    main()
