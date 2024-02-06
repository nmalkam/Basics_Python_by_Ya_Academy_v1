def even_cleanliness(num):
    # result = ''
    # for number in num:
    #     if int(number) % 2 == 0:
    #         result += str(number)
    # return result
    return ''.join([number for number in num if int(number) % 2 != 0])


assert even_cleanliness('1234') == '13'
assert even_cleanliness('123454321') == '13531'
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    num = input()
    print(even_cleanliness(num))


if __name__ == '__main__':
    main()
