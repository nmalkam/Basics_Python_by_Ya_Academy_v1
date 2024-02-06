def my_func(side_a, side_b, side_c):
    if side_a < side_b + side_c and side_b < side_a + side_c and side_c < side_a + side_b:
        return "YES"
    else:
        return "NO"


assert my_func(3, 3, 3) == "YES"
assert my_func(1, 2, 3) == "NO"
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    side_a = int(input())
    side_b = int(input())
    side_c = int(input())
    print(my_func(side_a, side_b, side_c))


if __name__ == '__main__':
    main()
