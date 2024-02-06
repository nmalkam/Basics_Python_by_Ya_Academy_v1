def my_func(p, v, t):
    # length = 43872
    i = 0
    count = 1
    b = [1, 22, 6, 3, 4]
    winner = {p: "Петя", v: "Вася", t: "Толя"}
    a = sorted(list(winner.keys()), reverse=True)
    # print(a)
    for _ in a:
        print(f"{count}. {winner[_]}")
        count += 1
        i += 1
    return b


# assert my_func(10, 5, 7) == "1. Петя\n2. Толя\n3. Вася"
# assert my_func(10, 11, 14) == "1. Толя\n2. Вася\n3. Петя"
# print("Успешное выполнение оператора assert")


def main():
    p = int(input())
    v = int(input())
    t = int(input())
    # print(my_func(p, v, t))
    my_func(p, v, t)


if __name__ == '__main__':
    main()
