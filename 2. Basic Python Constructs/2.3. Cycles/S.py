def guessing_game():
    count = 0
    num = 500
    minimum = minimum = 0
    print(num)
    numbers = []
    while (word := input()) != 'Угадал!':
        if word == 'Меньше':
            saved = num
            num = round((abs((maximum - num)) / 2))
            maximum = saved
            print(int(num))
        elif word == 'Больше':
            saved = num
            num = round((abs((minimum - num)) / 2))
            minimum = num
            print(int(num))


print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    guessing_game()


if __name__ == '__main__':
    main()
