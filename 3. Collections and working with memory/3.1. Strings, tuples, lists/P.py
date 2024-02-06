def news_announcement_2():

    length_of_anno = int(input())
    n = int(input())
    count = 0
    list_strings = []
    position_last_letter = length_of_anno

    while count != n:
        list_strings.append(input())
        count += 1
    for index, string in enumerate(list_strings):
        position_last_letter = position_last_letter - len(list_strings[index]) - 1
        if position_last_letter <= 0:
            position_last_letter = position_last_letter + len(list_strings[index]) + 1
            position_last_letter = len(list_strings[index]) - position_last_letter
            if string[position_last_letter - 1] == ' ':
                print(string[:position_last_letter - 1] + '...')
            else:
                print(string[:position_last_letter] + '...')
            break
        else:
            print(list_strings[index])


def main():
    news_announcement_2()


if __name__ == '__main__':
    main()
