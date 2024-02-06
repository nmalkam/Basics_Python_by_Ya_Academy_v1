def zaika_9():  # 3.2 Множества, словари зад. C и зад. E_v2

    d = {}

    while (string := input()) != '':
        for item in list(string.split()):
            d[item] = d.get(item, 0) + 1

    for key, val in d.items():
        print(f'{key} {val}')


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    zaika_9()


if __name__ == '__main__':
    main()
