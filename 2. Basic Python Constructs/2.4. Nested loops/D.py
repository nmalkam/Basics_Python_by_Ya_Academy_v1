def total_amount():  # -> (int):  # num: int):
    n = int(input())
    count = 0
    result = 0
    while count != n:
        num = input()
        for i in str(num):
            result += int(i)
        count += 1
    return result


def main():
    print(total_amount())


if __name__ == '__main__':
    main()
