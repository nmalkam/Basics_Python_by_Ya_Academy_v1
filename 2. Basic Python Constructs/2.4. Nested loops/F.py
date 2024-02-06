# ошибка в алгоритме вычисления, видимо считает для двух чисел НОД,
# а нужно для всех трёх

def NOD(first, second):  #

    item_NODs_list = []

    while first != 0 and second != 0:
        if first > second:
            if first % second == 0:
                item_NODs_list.append(second)
            first = first % second
        else:
            if second % first == 0:
                item_NODs_list.append(first)
            second = second % first
    return item_NODs_list
# я хочу решить следующим образом мне необходимо получить список и всех делителей
# возможно это не верно
# я пока не знаю как получить этот список,
# после получение наибольшего делителя программа заканчивает цикл
# а мне надо чтобы 40|2
#                  20|2
#                  10|2
#                   5|5
#                   1
# объяснение решения двумя способами: Нахождение НОД по алгоритму Евклида
# и с помощью разложения на простые множители
# http://www.cleverstudents.ru/divisibility/nod_finding.html#3_or_more


def NOD_2_0():

    all_NODs_list = []
    count = 0
    n = int(input())
    in_list = 0
    entrings = []

    if n == 1:
        return int(input())
    while count != n:
        entrings.append(int(input()))
        count += 1
    for number in entrings[:-1]:
        for number2 in entrings[1:]:
            if number != number2:
                all_NODs_list.append(NOD(number, number2))
    for item in sorted(all_NODs_list[0]):  # range(len(sorted(all_NODs_list[0])))
        for list in all_NODs_list:
            if item in list:
                in_list += 1
                if in_list == n:
                    return item

    return min(1, 2)


# нужно подавать в функцию нод все числа для первого значения в списке чисел,
# все для второго и тд

def main():
    print(NOD_2_0())


if __name__ == '__main__':
    main()
