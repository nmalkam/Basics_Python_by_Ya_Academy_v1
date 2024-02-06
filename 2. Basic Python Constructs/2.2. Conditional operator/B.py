def my_func(x, b):

    winner = {"Петя": x, "Вася": b}
    # winner = {}
    # winner[(input())] = "Петя"
    # winner[(input())] = "Вася"
    # print(max(winner, key=winner.get))
    # ) for _ in max(winner.values))
    return max(winner, key=winner.get)


# max(my_dict, key=my_dict.get)

assert my_func(10, 5) == "Петя"
assert my_func(10, 11) == "Вася"
print("Успешное выполнение оператора assert")

def main():
    # winner = {(input()): "Петя", (input()): "Вася"}

    x = int(input())
    b = int(input())
    print(my_func(x, b))


if __name__ == '__main__':
    main()
