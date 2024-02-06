def menu_blocks():

    list_dish = set()
    dishes_cooked = set()

    for _ in range(int(input())):
        list_dish.add(input())

    for _ in range(days := int(input())):
        for dish in range(meals := int(input())):
            dishes_cooked.add(input())
    if len(junction := list_dish ^ dishes_cooked) != 0:
        for item in sorted(junction):
            print(item)
    else:
        print('Готовить нечего')
    # print()


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    menu_blocks()


if __name__ == '__main__':
    main()
