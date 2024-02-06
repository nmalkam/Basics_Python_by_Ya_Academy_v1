def food_menu(n):

    menu_list = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
    index = 0
    count = 0

    while count != n:
        print(menu_list[index])
        index += 1
        count += 1
        if index == 5:
            index = 0


# assert food_menu(3) == 'Манная Гречневая Пшённая'
# assert food_menu(12) == 'Манная Гречневая Пшённая Овсяная Рисовая Манная ' \
#                         'Гречневая Пшённая Овсяная Рисовая Манная Гречневая'
# assert food_menu(4, 6) == 1
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    n = int(input())
    food_menu(n)


if __name__ == '__main__':
    main()
