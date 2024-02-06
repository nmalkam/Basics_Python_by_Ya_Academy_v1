def my_func(first, second, third):
    list_str = sorted((first, second, third))
    length = 10000
    # zaika: str = ""
    for item in list_str:
        if "зайка" in item:
            if len(item) < length:
                zaika = item
                length = len(item)
                if zaika > "":
                    # print(f"{zaika} {length}")
                    # print(zaika, length)
                    return f"{zaika} {length}"


# assert my_func("березка елочка зайка волк березка", "сосна сосна сосна елочка грибочки медведь",
#                "сосна сосна сосна белочка сосна белочка") == "березка елочка зайка волк березка 33"
# assert my_func("зайка березка", "березка зайка",
#                "березка елочка березка") == "березка зайка 13"
# assert my_func(" березка", "березка",
#                "березка елочка березка") == ""
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    first = input()
    second = input()
    third = input()
    print(my_func(first, second, third))


if __name__ == '__main__':
    main()
