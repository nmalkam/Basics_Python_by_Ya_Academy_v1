def zaika_10():

    strngs = []
    res = set()

    while (entered := input()) != '':
        # zeros = ['0']
        # for _ in entered.split():
        #     zeros.append(_)
        # zeros.append('0')
        strngs.append(entered.split())

    for _ in strngs:
        if len(_) == 1:
            continue
        for index, elem in enumerate(_):
            if elem == 'зайка':
                if index == 0:
                    res.add(_[index + 1])
                elif index == len(_) - 1:
                    res.add(_[index - 1])
                else:
                    res.add(_[index - 1])
                    res.add(_[index + 1])

    for _ in res:
        print(_)
    # print()


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():

    zaika_10()


if __name__ == '__main__':
    main()
