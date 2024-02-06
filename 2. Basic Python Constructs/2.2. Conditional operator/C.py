def my_func(p, v, t):
    # length = 43872
    winner = {"Петя": p, "Вася": v, "Толя": t}
    return max(winner, key=winner.get)


# max(my_dict, key=my_dict.get)
assert my_func(10, 5, 7) == "Петя"
assert my_func(10, 11, 14) == "Толя"


def main():
    p = int(input())
    v = int(input())
    t = int(input())
    print(my_func(p, v, t))


if __name__ == '__main__':
    main()
