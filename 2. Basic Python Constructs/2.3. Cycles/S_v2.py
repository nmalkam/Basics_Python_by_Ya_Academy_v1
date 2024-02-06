def guessing_game():
    halfs = [500, 250, 125, 63, 32, 16, 8, 4, 2, 1]
    num = 500
    print(num)
    halfs_position = 1
    while (word := input()) != 'Угадал!':
        if word == 'Меньше':
            num = round(num - halfs[halfs_position])
            halfs_position += 1
            print(num)
        elif word == 'Больше':
            num = round(num + halfs[halfs_position])
            halfs_position += 1
            print(num)


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    guessing_game()


if __name__ == '__main__':
    main()
