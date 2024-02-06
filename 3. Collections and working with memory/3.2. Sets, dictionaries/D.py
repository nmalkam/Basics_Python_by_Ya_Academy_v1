def porridge_eater() -> str:

    semolina_lst = set()
    oatmeal_lst = set()

    n = int(input())
    m = int(input())

    for _ in range(n):
        semolina_lst.add(input())
    for _ in range(m):
        oatmeal_lst.add(input())
    if len(junction := semolina_lst & oatmeal_lst) != 0:
        return str(len(junction))
    else:
        return 'Таких нет'


# assert porridge_eater() == "1. Петя\n2. Толя\n3. Вася"
# assert porridge_eater() == "1. Толя\n2. Вася\n3. Петя"
# print("Успешное выполнение оператора assert")


def main():
    print(porridge_eater())


if __name__ == '__main__':
    main()
