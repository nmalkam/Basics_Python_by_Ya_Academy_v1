def kid_counter(x, y):
    swap = 0
    if x > y:
        x, y = y, x
        swap = 1
    result = ''
    num_list = []
    for i in range(x, y + 1):
        num_list.append(i)
    if swap == 1:
        reswaped = num_list[::-1]
        for num in reswaped:
            result = " ".join([result, str(num)])
    else:
        for num in num_list:
            result = " ".join([result, str(num)])
    return result[1:]


assert kid_counter(1, 10) == "1 2 3 4 5 6 7 8 9 10"
assert kid_counter(3, -3) == "3 2 1 0 -1 -2 -3"
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    x = int(input())
    y = int(input())
    print(kid_counter(x, y))


if __name__ == '__main__':
    main()
