# Sergey Klochko, [27.08.2023 20:55]
# тут есть два подхода:
# 1) вы придумываете функцию, которая в зависимости от i и j выдает вам правмильное число.
# 2) вы придумываете как пройти по матрице таким маршрутом и попутно прописываете в ячейки следующее значение из последовательности от единицы до m*n.
#
# Sergey Klochko, [27.08.2023 21:06]
# функция в данном случае это формула
#
# Sergey Klochko, [27.08.2023 21:34]
# есть еще третий путь.
# для совсем ленивых, но сообразительных.
#
# сделать матрицу обратной размерности по алгоритму из предыдущей задачи, а потом просто при выводе поменять местами высоту и ширину
def number_snake_2(height: int, width: int):

    cell_width = len(str(width * height))
    pos = 1
    number = 1
    cycle = 1

    for i in range(1, height + 1):
        for j in range(1, width + 1):
            print(f'{number:>{cell_width}}', end=' ')
            if j % 2 != 0:  # and i % 2 != 0:
                number += (2 * (height - i)) + 1
            # elif i % 2 == 0:
            #     number += (2 * (height - i)) + 1
            else:
                number += 1
            if pos == width:
                print()
                pos = 1
                number = 1 + cycle
                cycle += 1
                # if j % 2 != 0:
                #     number += width - 1
                # else:
                #     number += width + 1
            else:
                pos += 1


# assert number_snake_2(2, 3) == 1
assert number_snake_2(4, 6) == 1


def main():
    height, width = [int(input()) for _ in range(2)]
    number_snake_2(height, width)


if __name__ == '__main__':
    main()


    # for _ in range(height):
    #     for _ in range(width):
    #         if pos == 1:
    #             print(f'{number:>{cell_width}}', end=' ')
    #         else:
    #             print(f'{(number + height):>{cell_width}}', end=' ')
    #             number += height
    #         if pos == width:
    #             print()
    #             pos = 1
    #             number = 1 + cycle
    #             cycle += 1
    #         else:
    #             pos += 1


    # while num <= n * m:
    #     for i in range(m):
    #         if num <= m:
    #             print(num, end=' ')
    #             num += 1
    #         else:
    #             break
    #     print()
    #     count += 1

