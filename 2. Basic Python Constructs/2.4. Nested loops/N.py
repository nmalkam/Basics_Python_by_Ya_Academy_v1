def number_snake(height: int, width: int):

    cell_width = len(str(width * height))
    pos = 1
    number = 1

    for i in range(1, height + 1):  # range(height):
        for j in range(width):
            print(f'{number:>{cell_width}}', end=' ')
            if i % 2 != 0:
                number += 1
            else:
                # print(f'{number:>{cell_width}}', end=' ')
                number -= 1
            if pos == width:
                print()
                pos = 1
                if i % 2 != 0:
                    number += width - 1
                else:
                    number += width + 1
            else:
                pos += 1


# assert number_snake(2, 3) == 1
# assert number_snake(4, 6) == 1


def main():
    height, width = [int(input()) for _ in range(2)]
    number_snake(height, width)


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
