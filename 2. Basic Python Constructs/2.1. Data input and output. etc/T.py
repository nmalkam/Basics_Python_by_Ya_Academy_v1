def my_func(first, second, third):
    list_str = sorted((first, second, third))
    # print(1)
    # print(list_str)
    # print(len(first))
    # print(len(second))
    # print(len(third))
    coincidence_list = []
    for item in list_str:
        print(item)
        print(len(item))
        if "зайка" in item:
            coincidence_list.append(item)
            lenght = len(coincidence_list)
            # len(coincidence_list)
        # print(lenght)
            # print(coincidence_list)
        # print(sorted(coincidence_list), len(sorted(map(str, coincidence_list))))
        # return sorted(coincidence_list), len(item)


assert my_func("березка елочка зайка волк березка", "сосна сосна сосна елочка грибочки медведь",
               "сосна сосна сосна белочка сосна белочка") == "березка елочка зайка волк березка", 33
# assert my_func("зайка березка", "березка зайка",
#                "березка елочка березка") == "березка зайка", 13
print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    first = input()
    second = input()
    third = input()
    print(my_func(first, second, third))


if __name__ == '__main__':
    main()
