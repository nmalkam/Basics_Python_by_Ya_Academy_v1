def is_prime(num):
    if num == 1:
        return "NO"
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return "NO"
    return "YES"


# assert is_prime(6) == "NO"
# assert is_prime(90999899) == "YES"
# assert is_prime(67) == "YES"
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    num = int(input())
    print(is_prime(num))


if __name__ == '__main__':
    main()

