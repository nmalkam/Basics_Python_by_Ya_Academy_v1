# неправильно
def my_func(x, num):
    n = 0
    while n != num:
        print(x)
        n += 1


# assert my_func("2 + 2 = 4", 3) == ['2 + 2 = 4', '2 + 2 = 4', '2 + 2 = 4']
# assert my_func("Нельзя нажимать неизвестные кнопки!", 4) ==['Нельзя нажимать неизвестные кнопки!',
#                                                             'Нельзя нажимать неизвестные кнопки!',
#                                                             'Нельзя нажимать неизвестные кнопки!',
#                                                             'Нельзя нажимать неизвестные кнопки!']
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    x = input()
    num = int(input())
    my_func(x, num)


if __name__ == '__main__':
    main()
