def my_func(first, second, third):
    ns = (first, second, third)
    for d in ns:
        if d.find('зайка') > 0:
            print(d, len(d))


assert my_func("березка елочка зайка волк березка", "сосна сосна сосна елочка грибочки медведь",
               "сосна сосна сосна белочка сосна белочка") == "березка елочка зайка волк березка 33"
assert my_func("зайка березка", "березка зайка",
               "березка елочка березка") == "березка зайка 13"
assert my_func(" березка", "березка",
               "березка елочка березка") == ""
print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    first = input()
    second = input()
    third = input()
    print(my_func(first, second, third))


if __name__ == '__main__':
    main()
