# https://ru.stackoverflow.com/questions/1056933/%D0%9E%D0%B1%D1%8A%D1%8F%D1%81%D0%BD%D0%B8%D1%82%D0%B5-%D0%BF%D0%BE%D0%B6%D0%B0%D0%BB%D1%83%D0%B9%D1%81%D1%82%D0%B0-%D0%BC%D0%BD%D0%B5-%D1%8D%D1%82%D1%83-%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D1%83-%D0%9F%D0%BE%D1%87%D0%B5%D0%BC%D1%83-h-m-r-%D0%BD%D0%B0%D1%85%D0%BE%D0%B4%D1%8F%D1%82%D1%81%D1%8F-%D0%B8%D0%BC%D0%B5%D0%BD%D0%BD%D0%BE-%D1%82%D0%B0%D0%BA?newreg=63b089a722d340e8a925a12efc920987
# осторожно там есть решение
# last_h = 0
#     for i in range(int(input())):
#         block = int(input())
#         now_h = block % 256  # "первый разряд" от умножения на 256
#         r = (block // 256) % 256  # "средний разряд" от умножения на 256
#         m = block // 256 ** 2  # "крайний разряд" от умножения на 256
#         calc_h = (37 * (m + r + last_h)) % 256  # хеш по формуле
#         if calc_h != now_h or calc_h > 100:
#             print(i)
#             break
#         last_h = calc_h
#     else:
#         print(-1)
def Blockchain():
    import random
    last_h = 0
    for i in range(int(input())):
        block = int(input())
        now_h = block % 256
        r = (block // 256) % 256
        m = block // 256 ** 2
        calc_h = (37 * (m + r + last_h)) % 256
        if calc_h != now_h or calc_h > 100:
            return i
            break
        last_h = calc_h
    else:
        return -1
    # Я
    # кажется
    # понял, это
    # работает
    # как
    # с
    # разрядами
    # десятков: bn = hn + rn * 256 + mn * 256 ** 2, мы
    # сдвигаем
    # каждый
    # элемент
    # на
    # разряд.например(пример
    # в
    # нашей
    # любимой
    # 10
    # ричной
    # системе
    # исчисления): n = first + second * 10 + third * (10 ** 2)
    # n = str(first) + str(second) + str(third)
    # т.е.и
    # в
    # первом
    # и
    # во
    # втором
    # случае
    # они
    # идут
    # друг
    # за
    # другом.Поэтому
    # мы
    # и
    # можем
    # вытаскивать
    # по
    # разряду
    # из
    # блока


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    print(Blockchain())


if __name__ == '__main__':
    main()
