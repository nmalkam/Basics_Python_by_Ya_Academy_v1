def porridge_eater_2() -> str:

    d = {}
    pupils_count = 0

    n = int(input())
    m = int(input())

    for _ in range(n + m):
        surname = input()
        d[surname] = d.get(surname, 0) + 1
    for val in d.values():
        if val == 1:
            pupils_count += 1
    if pupils_count > 1:
        return str(pupils_count)
    else:
        return 'Таких нет'


# print("Успешное выполнение оператора assert")


def main():
    print(porridge_eater_2())


if __name__ == '__main__':
    main()
