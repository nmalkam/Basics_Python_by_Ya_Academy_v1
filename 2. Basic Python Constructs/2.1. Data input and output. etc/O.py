def my_func(x, b):
    list_num = sorted(map(int, (str(x) + str(b))))
    # minimum = 9
    # maximum = 0
    # for item in list_num:
    #     if item < minimum:
    #         minimum = item
    #     if item > maximum:
    #         maximum = item
    min_num = list_num.pop(0)
    max_num = list_num.pop(-1)
    sums = (list_num[0] + list_num[1]) % 10
    # sums = map(lambda i: (list_num[0] + list_num[1]) % 10)
    # print(list_num)
    # print(min_num)
    # print(max_num)
    # print(sums)
    # print(str(max_num) + str(sums) + str(min_num))
    return str(max_num) + str(sums) + str(min_num)


assert my_func(31, 11) == "321"
assert my_func(49, 17) == '911'
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    x = int(input())
    b = int(input())
    print(my_func(x, b))


if __name__ == '__main__':
    main()
