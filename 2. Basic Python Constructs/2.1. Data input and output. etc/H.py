def my_func(x):
    if "зайка" in x:
        return "YES"
    else:
        return "NO"


assert my_func("березка елочка зайка волк березка") == "YES"
assert my_func("сосна сосна сосна елочка грибочки медведь") == "NO"
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    x = input()
    print(my_func(x))


if __name__ == '__main__':
    main()
