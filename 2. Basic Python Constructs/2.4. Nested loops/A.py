def multiplication_table(num: int):  # -> str:
    list_j = []
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            list_j.append(str(j * i))
            if j == num:
                result = ' '.join(list_j)
                print(result)
                list_j = []


# assert multiplication_table(3) == ['1 2 3', '2 4 6', '3 6 9']
# assert multiplication_table(5) == [f'1 2 3 4 5\n'
#                                    f'2 4 6 8 10\n'
#                                    f'3 6 9 12 15\n'
#                                    f'4 8 12 16 20\n'
#                                    f'5 10 15 20 25']


def main():
    num = int(input())
    multiplication_table(num)


if __name__ == '__main__':
    main()
