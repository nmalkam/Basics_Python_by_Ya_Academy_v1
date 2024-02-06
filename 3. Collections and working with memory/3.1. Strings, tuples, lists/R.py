def RLE(n: str):

    count = 0
    res = 0
    last_digit = n[0]

    while count != len(n):
        if n[count] == last_digit:
            res += 1
        else:
            print(n[count - 1], res)
            last_digit = n[count]
            res = 1
        count += 1
    print(n[-1], res)
    # for index, num in enumerate(n):
    #     if num == last_digit:
    #         res += 1
    #     else:
    #         print(n[index - 1], res)
    #         last_digit = num
    #         res = 1
    # print(n[-1], res)


assert RLE('010000100001111111110111110000000000000011111111') == 0  # 0 14 1 8
# assert RLE(0110000000100001000) == 1
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():

    n = input()

    RLE(n)


if __name__ == '__main__':
    main()
