# Корень зла 2 из 2.2 Q Корень зла
def my_func(a, b, c):
    d = b ** 2 - 4 * a * c
    if a == b == c == 0:
        return "Infinite solutions"
    elif a == b == 0 and c != 0:
        return "No solution"
    elif a == c == 0 and b != 0:
        x1 = 0
        return f'{x1:.2f}'
    elif a == 0 and c != 0 and b != 0:
        x1 = -c / b
        # print(f'{x1:.2f}')
        return round(x1, 2)
        # return f'{x1:.2f}'
    else:
        if d == 0:
            x1 = -b / (2 * a)
            # print(f'{x1:.2f}')
            return round(x1, 2)
            # return f'{x1:.2f}0'
        elif d > 0:
            x1 = (-b - d ** 0.5) / (2 * a)
            x2 = (-b + d ** 0.5) / (2 * a)
            if x1 < x2:
                return f"{x1:.2f} {x2:.2f}"
            else:
                return f"{x2:.2f} {x1:.2f}"
        elif d < 0:
            return "No solution"


# assert my_func(1, -2, 1) == 1.00
# assert my_func(3.5, -2.4, -7.3) == "-1.14 1.83"
# assert my_func(1, 0, 0) == 0.00
# assert my_func(1, 0, 1) == "No solution"
# assert my_func(1, 1, 0) == "-1.00 0.00"
# assert my_func(0, 0, 1) == "No solution"
# assert my_func(0, 0, 0) == "Infinite solutions"
# assert my_func(0, 3, 1) == -0.33
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    first = float(input())
    second = float(input())
    third = float(input())
    print(my_func(first, second, third))


if __name__ == '__main__':
    main()
