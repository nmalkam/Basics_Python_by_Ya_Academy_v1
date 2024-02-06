def porridge_eater_3():

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
        for item in sorted(junction):
            print(item)
    else:
        print('Таких нет')


# assert porridge_eater_3() == "1. Толя\n2. Вася\n3. Петя"
# print("Успешное выполнение оператора assert")


def main():
    porridge_eater_3()


if __name__ == '__main__':
    main()
