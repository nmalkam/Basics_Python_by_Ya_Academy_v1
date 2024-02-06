def my_func(n, m):
    pe = 7 - 3 + 2 + n
    va = 6 + 3 + m
    # to = -2.2.Conditional operator
    # ge = 2.2.Conditional operator
    return "Петя" if pe > va else "Вася"


assert my_func(3, 5) == "Вася"
print("Успешное выполнение оператора assert")


def main():
    n = int(input())
    m = int(input())
    print(my_func(n, m))


if __name__ == '__main__':
    main()
