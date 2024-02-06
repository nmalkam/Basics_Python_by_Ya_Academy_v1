def my_func(x):
    if x % 400 == 0:
        return "YES"
    elif x % 100 == 0:
        return "NO"
    elif x % 4 == 0:
        return "YES"
    else:
        return "NO"
    # return "YES" if (x % 4 == 0 and x % 400 == 0) else "NO"


assert my_func(2022) == "NO"
assert my_func(2020) == "YES"
assert my_func(1900) == "NO"
assert my_func(2000) == "YES"
# print("Успешно! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    x = int(input())
    print(my_func(x))


if __name__ == '__main__':
    main()
