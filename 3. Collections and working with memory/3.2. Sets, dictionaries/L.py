def namesakes_2():

    list_res = []
    d = {}

    for _ in range(int(input())):
        surname = input()
        d[surname] = d.get(surname, 0) + 1

    for key, val in set(d.items()):
        if val > 1:
            list_res.append(f'{key} - {val}')
    for item in sorted(list_res):
        print(item)
    if not list_res:
        print('Однофамильцев нет')


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    namesakes_2()


if __name__ == '__main__':
    main()
