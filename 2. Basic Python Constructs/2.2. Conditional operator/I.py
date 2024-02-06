def my_func(x, b, th):
    if x < b and x < th:
        return x
    elif b < x and b < th:
        return b
    else:
        return th


assert my_func("Вова", "Аня", "Боря") == "Аня"
assert my_func("Толя", "Коля", "Вася") == "Вася"
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    x = input()
    b = input()
    th = input()
    print(my_func(x, b, th))


if __name__ == '__main__':
    main()
