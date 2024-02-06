def zaika8():  # 3.1. Строки, кортежи, списки H. Зайка — 7

    # count = 0
    # surround = []
    items = set()
    n = int(input())

    # while count != n:
    #     string = input()
    #     words_list = string.split()
    #     for word in words_list:
    #         if word not in surround:
    #             surround.append(word)
    #     count += 1
    for _ in range(int(input())):
        string = input()
        items = items | set(string.split())

    for item in items:
        print(item)


# assert zaika8("березка елочка зайка волк березка") == "YES"
# assert zaika8("сосна сосна сосна елочка грибочки медведь") == "NO"
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    zaika8()


if __name__ == '__main__':
    main()
