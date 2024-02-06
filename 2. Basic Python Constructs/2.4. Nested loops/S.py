def number_square(n: int):

    cell_width = len(str((n + 1) // 2))

    for i in range(n):
        for j in range(n):
            print(f'{min(i + 1, j + 1, abs(n - i), abs(n - j)):>{cell_width}}', end=' ')
        print()


# assert number_square(3) == "Опасность! Покиньте зону как можно скорее!"
# assert number_square(5) == "Зона безопасна. Продолжайте работу."
# assert number_square(8) == "Вы вышли в море и рискуете быть съеденным акулой!"


def main():
    n = int(input())

    number_square(n)


if __name__ == '__main__':
    main()
