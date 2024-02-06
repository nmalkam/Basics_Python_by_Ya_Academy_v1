def smallest_name():
    n = 1
    num = int(input())
    max_name = 'ЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯ'
    while n <= num:
        if (new_name := input()) < max_name:
            max_name = min(new_name, max_name)
        n += 1
    # print(max_name)
    return max_name


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    print(smallest_name())


if __name__ == '__main__':
    main()

# sum(int(digit) for digit in input())
# sum(map(int, input()))
