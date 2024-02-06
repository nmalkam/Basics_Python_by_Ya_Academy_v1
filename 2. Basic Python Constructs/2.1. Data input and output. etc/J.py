def my_func(x):
    unit = x % 10
    tens = int(x / 10) % 10
    sum_units = unit + tens
    # print(sum_units)
    huns = int(x / 100) % 10
    sum_hun = tens + huns
    # print(sum_hun)
    num_list = [sum_hun, sum_units]
    # print(num_list)
    sorted_list = sorted(num_list, reverse=True)
    # print(sorted_list)
    result = str(sorted_list[0]) + str(sorted_list[1])
    # result = ''.join([c for c in sorted_list if c.isdigit()])
    # print(result[0])
    # print(result)
    return result


assert my_func(123) == "53"
# assert my_func(741) == "115"
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    x = int(input())
    print(my_func(x))


if __name__ == '__main__':
    main()
