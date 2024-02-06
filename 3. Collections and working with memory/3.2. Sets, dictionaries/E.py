def porridge_eater_2() -> str:

    semolina_lst = set()
    oatmeal_lst = set()

    n = int(input())
    m = int(input())

    for _ in range(n + m):
        surname = input()
        if surname in semolina_lst:
            oatmeal_lst.add(surname)
        else:
            semolina_lst.add(surname)
    if len(junction := semolina_lst ^ oatmeal_lst) != 0:
        return str(len(junction))
    else:
        return 'Таких нет'


# assert porridge_eater_2() == "1. Петя\n2. Толя\n3. Вася"
# assert porridge_eater_2() == "1. Толя\n2. Вася\n3. Петя"
# print("Успешное выполнение оператора assert")


def main():
    print(porridge_eater_2())


if __name__ == '__main__':
    main()
