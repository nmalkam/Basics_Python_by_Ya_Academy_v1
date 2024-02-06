def kid_counter(x, y):
    result = ""
    num_list = []
    for i in range(x, y + 1):
        num_list.append(i)
    for num in num_list:
        result = " ".join([result, str(num)])
    # result.remove(" ")
    # print(result[1:])
    return result[1:]


# assert kid_counter(0, 0) == 0
# assert kid_counter(1, 10) == "1 2 3 4 5 6 7 8 9 10"
# assert kid_counter(-3, 3) == "-3 -2 -1 0 1 2 3"
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")

def main():
    x = int(input())
    y = int(input())
    print(kid_counter(x, y))


if __name__ == '__main__':
    main()
