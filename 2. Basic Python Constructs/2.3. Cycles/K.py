def my_func(num):
    return sum(int(x) for x in num)


assert my_func(12345) == 15
assert my_func(100500) == 6
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    num = input()
    print(my_func(num))


if __name__ == '__main__':
    main()

# sum(int(digit) for digit in input())
# sum(map(int, input()))
