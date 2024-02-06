def my_func(x):
    n = 1
    fa = 1
    while n != x + 1:
        fa = fa * n
        n += 1
    return fa


assert my_func(3) == 6
assert my_func(0) == 1
assert my_func(5) == 120
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    x = int(input())
    print(my_func(x))


if __name__ == '__main__':
    main()
