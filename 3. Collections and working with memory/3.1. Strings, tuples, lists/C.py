def news_announcement():
    length_of_anno = int(input())
    n = int(input())
    count = 0
    while count != n:
        string = input()
        if len(string) > length_of_anno:
            print(string[:length_of_anno - 3] + '...')
            # res = string[:l - 2]+'...'
            # print(len(res))
            # print(res)
        else:
            print(string)
        count += 1


# assert news_announcement() == "Петя"
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    news_announcement()


if __name__ == '__main__':
    main()
