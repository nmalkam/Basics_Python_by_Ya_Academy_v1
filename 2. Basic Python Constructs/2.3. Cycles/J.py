def route():
    hor = ver = 0
    while (word := input()) != 'СТОП':
        if word == 'СЕВЕР':
            ver += int(input())
        elif word == 'ЮГ':
            ver -= int(input())
        elif word == 'ЗАПАД':
            hor -= int(input())
        elif word == 'ВОСТОК':
            hor += int(input())
    return f'{ver}\n{hor}'


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    print(route())


if __name__ == '__main__':
    main()
