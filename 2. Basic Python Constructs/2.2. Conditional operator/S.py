def coordinates_for_island(x, y):
    little_quarter_r = (25 - (x ** 0.5) ** 4) ** 0.5
    little_quarter_abs = abs(little_quarter_r)
    parabola = 0.25 * x ** 2 + 0.5 * x + 8.75
    inclined_line = 5 / 3 * (x + 7)
    straight_line = 0 * (x + 4) + 5
    if (x - 0) ** 2 / 10 ** 2 + (y - 0) ** 2 / 10 ** 2 >= 1:
        print("Вы вышли в море и рискуете быть съеденным акулой!")
        return
    elif little_quarter_abs <= 5:
        if inclined_line >= y:
            if straight_line >= y:
                if parabola <= y:
                    print("Опасность! Покиньте зону как можно скорее!")
                    return
    print("Зона безопасна. Продолжайте работу.")
    return


# assert coordinates_for_island(0, 5) == "Опасность! Покиньте зону как можно скорее!"
# assert coordinates_for_island(5, 0) == "Опасность! Покиньте зону как можно скорее!"
# assert coordinates_for_island(2, 2) == "Опасность! Покиньте зону как можно скорее!"
# assert coordinates_for_island(2, -2) == "Опасность! Покиньте зону как можно скорее!"
# assert coordinates_for_island(-4, -4) == "Опасность! Покиньте зону как можно скорее!"
# assert coordinates_for_island(-6, -8) == "Зона безопасна. Продолжайте работу."
# assert coordinates_for_island(-2, 2) == "Опасность! Покиньте зону как можно скорее!"
# assert coordinates_for_island(3.5, -3.2) == "Опасность! Покиньте зону как можно скорее!"
# assert coordinates_for_island(-5.2, 3.4) == "Зона безопасна. Продолжайте работу."
# assert coordinates_for_island(18, 0) == "Вы вышли в море и рискуете быть съеденным акулой!"
# assert coordinates_for_island(4, -4) == "Зона безопасна. Продолжайте работу."


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    x = float(input())
    y = float(input())
    coordinates_for_island(x, y)


if __name__ == '__main__':
    main()
