def my_func(x):
    list_num = list(map(int, x))
    minimum = min(list_num)
    maximum = max(list_num)
    list(map(list_num.remove, (minimum, maximum)))
    middle = list_num[0]
    # print(list_num)
    # print(minimum)
    # print(maximum)
    # print(middle)
    if minimum == 0:
        les = str(middle) + str(minimum)
    else:
        les = str(minimum) + str(middle)
    high = str(maximum) + str(middle)
    print(f"{les} {high}")
    return f"{les} {high}"


assert my_func("996") == "69 99"
assert my_func("103") == "10 31"
assert my_func("787") == "77 87"
assert my_func("909") == "90 99"
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    x = input()
    print(my_func(x))


if __name__ == '__main__':
    main()
