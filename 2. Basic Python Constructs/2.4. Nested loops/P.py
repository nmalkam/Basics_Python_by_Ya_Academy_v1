# https://reshebnik.mumuproject.com/frontpage/yandex-python-handbook/yandex-python-2-4-vlozhennye-cikly/yandex-handbook-redizain-tablicy-umnozheniya/
# В примерах даны только квадратные матрицы и это создает ощущение, что входные данные составляют не размер таблицы и ширину ячейки, а собственно высоту и ширину таблицы
# либо просто возьми мои ассерты
def redesign_multiplication_table(dim: int, width: int):

    slash = '-'
    pos = 1

    for i in range(1, dim + 1):
        for j in range(1, dim + 1):
            if pos == dim:
                print(f'{i * j:^{width}}')
            else:
                print(f'{i * j:^{width}}', end='|')
            if pos == dim:
                pos = 1
            else:
                pos += 1
        if i != dim:
            print(f'{(slash * width * dim) + (slash * (dim - 1))}')


assert redesign_multiplication_table(3, 30) == 1
assert redesign_multiplication_table(15, 5) == 1


def main():
    dim, width = [int(input()) for _ in range(2)]
    redesign_multiplication_table(dim, width)


if __name__ == '__main__':
    main()

#   1  |  2  |  3  |  4  |  5
# -----------------------------
#   2  |  4  |  6  |  8  | 10
# -----------------------------
#   3  |  6  |  9  | 12  | 15
# -----------------------------
#   4  |  8  | 12  | 16  | 20
# -----------------------------
#   5  | 10  | 15  | 20  | 25
#  1 | 2 | 3
# -----------
#  2 | 4 | 6
# -----------
#  3 | 6 | 9
