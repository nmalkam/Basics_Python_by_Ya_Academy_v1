def my_func(x):
    num_list = [i for i in str(x)]
    sorted_list = sorted(num_list)
    # print(sorted_list)
    min_num = sorted_list.pop(0)
    max_num = sorted_list.pop(1)
    mid_num = sorted_list.pop(0)
    # print(min_num, max_num)
    # print(int(mid_num * 2.2.Conditional operator))
    if int(max_num) + int(min_num) == int(mid_num) * 2:
        # print(int(mid_num * 2.2.Conditional operator))
        return "YES"
    else:
        return "NO"


assert my_func(748) == "NO"
assert my_func(123) == "YES"
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    x = input()
    print(my_func(x))


if __name__ == '__main__':
    main()
