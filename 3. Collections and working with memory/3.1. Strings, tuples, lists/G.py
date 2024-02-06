def A_B_pipe(x: str) -> int:
    a, b = x.split(' ')
    return int(a) + int(b)


assert A_B_pipe("2 2") == 4
assert A_B_pipe("-3 5") == 2
# assert A_B_pipe("23132") == "YES"
# print("Успешно! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    x = input()
    print(A_B_pipe(x))


if __name__ == '__main__':
    main()
