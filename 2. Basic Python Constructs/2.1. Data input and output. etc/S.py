def my_func(x, y):
    from math import sqrt
    y = sqrt(1 - (sqrt(x))**4)  #окружность



    # if (x - xk) ** 2.2.Conditional operator / 5 ** 2.2.Conditional operator + (y - yk) ** 2.2.Conditional operator / 5 ** 2.2.Conditional operator < 1 or :
        # print("Введите координаты точки: ")
        # x = float(input("x = "))
        # y = float(input("y = "))
        # print("Введите центр окружности и его радиус: ")
        # r = float(input("R = "))
        # xk = float(input("x(k) = "))
        # yk = float(input("y(k) = "))


assert my_func(3.5, -3.2) == "Опасность! Покиньте зону как можно скорее!"
assert my_func(-5.2, 3.4) == "Зона безопасна. Продолжайте работу."
assert my_func(8, 0) == "Вы вышли в море и рискуете быть съеденным акулой!"
print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    x = int(input())
    y= int(input())
    print(my_func(x, y))


if __name__ == '__main__':
    main()
