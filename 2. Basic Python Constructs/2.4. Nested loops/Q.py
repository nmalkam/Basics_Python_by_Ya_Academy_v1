# 2.3. Cycles/P.py

def palindrome() -> int:

    # list_p = []
    count = 0
    res = 0
    n = int(input())

    while n != count:
        num = str(input())
        if num == num[::-1]:
            res += 1
        count += 1
    return res


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    print(palindrome())


if __name__ == '__main__':
    main()
