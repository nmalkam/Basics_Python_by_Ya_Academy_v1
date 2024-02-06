# эта задача выполняется верно, но я не понял задание
# [2;10] — основание системы счисления
# строчка выше всё же означает систему счисления от 2 до 10
# включая каждую цифру входящую в этот диапазон, то есть 2,3,4,5....

def mathematical_benefit(decimal_num: int) -> int:
    """В моём примере просят: Формат вывода
Одно натуральное число из диапазона [2;10] — основание системы счисления
с максимальной выгодой.
Если таких оснований несколько, выбирается наименьшее. """

    sum_num = {}
    dict_num_NS = {}  # number systems = системы счисления
    num_10_to_2 = []  # список из 10СИ в 2СИ (СИСТЕМА ИСЧИСЛЕНИЯ, здесь и далее)
    binary_number = decimal_num

    dict_num_NS[10] = decimal_num
    sum_num[10] = sum(map(int, str(decimal_num)))

    while binary_number > 1:
        num_10_to_2.append(int(binary_number % 2))
        binary_number /= 2
    binary_number = int(''.join(map(str, num_10_to_2[::-1])))
    dict_num_NS[2] = binary_number
    sum_num[2] = sum(map(int, num_10_to_2[::-1]))

    # Добавление нулей в начало, если необходимо
    while len(str(binary_number)) % 3 != 0:
        binary_number = '0' + str(binary_number)

    # Разделение на группы по три цифры
    groups = [binary_number[i:i + 3] for i in range(0, len(binary_number), 3)]

    # Создание словаря для замены групп на восьмеричные цифры
    binary_to_octal = {
        '000': '0',
        '001': '1',
        '010': '2',
        '011': '3',
        '100': '4',
        '101': '5',
        '110': '6',
        '111': '7'
    }

    # Замена групп на восьмеричные цифры
    octal_number = ''.join(binary_to_octal[group] for group in groups)

    dict_num_NS[8] = int(octal_number)
    sum_num[8] = sum(map(int, octal_number))

    # print(max(sum_num.values()) for )
    # return max(sum_num.values())
    # print(max(sum_num, key=sum_num.get))
    return max(sum_num, key=sum_num.get)


# assert mathematical_benefit(44) == 101100
# assert mathematical_benefit(12) == 7  # 1100
# assert mathematical_benefit(52) == 9  # 110100
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():

    num = int(input())

    print(mathematical_benefit(num))


if __name__ == '__main__':
    main()

# a = int(input("Введите десятичное число>"))
# print("Восьмеричное число: %s"  %  oct(a))
