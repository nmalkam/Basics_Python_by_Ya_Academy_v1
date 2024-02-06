def zaika_10():

    strngs = []
    res = set()

    while (entered := input()) != '':
        zeros = ['0']
        for _ in entered.split():
            zeros.append(_)
        zeros.append('0')
        strngs.append(zeros)

    for _ in strngs:
        for index, elem in enumerate(_):
            if elem == 'зайка':
                if _[index - 1] != '0':
                    res.add(_[index - 1])
                if _[index + 1] != '0':
                    res.add(_[index + 1])

    for _ in res:
        print(_)
    # print()


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():

    zaika_10()


if __name__ == '__main__':
    main()
