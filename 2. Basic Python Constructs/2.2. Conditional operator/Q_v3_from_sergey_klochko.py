def my_func(a, b, c):
    from math import sqrt
    if a == b == c == 0:
        return "No solution"
    elif a == 0 and b != 0 and c != 0:
        return "No solution"
    elif a == b == 0:
        # your code here
        pass
    elif a == c == 0:
        # your code here
        pass
    else:
        disc = (b ** 2) - (4 * a * c)
        if disc == 0:
            # your code here
            pass
        elif disc > 0:
            # your code here
            pass
        else:
            # your code here
            pass


assert my_func(1, -2, 1) == 1.00
assert my_func(3.5, -2.4, -7.3) == "-1.14 1.83"
assert my_func(1, 0, 0) == 0
assert my_func(1, 0, 1) == "No solution"
assert my_func(1, 1, 0) == "-1.00 0.00"
assert my_func(0, 0, 1) == "No solution"
assert my_func(0, 0, 0) == "No solution"
assert my_func(0, 3, 1) == "0.33"
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    first = float(input())
    second = float(input())
    third = float(input())
    print(my_func(first, second, third))


if __name__ == '__main__':
    main()
