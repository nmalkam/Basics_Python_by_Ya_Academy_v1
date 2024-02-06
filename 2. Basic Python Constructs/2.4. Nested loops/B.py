def not_multiplication_table(num: int):  # -> str:
    # num = input()
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            print(f'{j} * {i} = {j * i}')


def main():
    num = int(input())
    not_multiplication_table(num)


if __name__ == '__main__':
    main()
