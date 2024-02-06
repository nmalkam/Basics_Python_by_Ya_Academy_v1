def number_rectangle_2(height, width):

    cell_width = len(str(width * height))

    cycle = 1
    pos = 1
    number = 1

    for _ in range(height):
        for _ in range(width):
            if pos == 1:
                print(f'{number:>{cell_width}}', end=' ')
            else:
                print(f'{(number + height):>{cell_width}}', end=' ')
                number += height
            if pos == width:
                print()
                pos = 1
                number = 1 + cycle
                cycle += 1
            else:
                pos += 1


# assert number_rectangle_2(3, 4) == 1
# assert number_rectangle_2(2, 3) == 1
# assert number_rectangle_2(4, 6) == 1
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    height = int(input())
    width = int(input())
    number_rectangle_2(height, width)


if __name__ == '__main__':
    main()

# Решение с вложенными циклами

# dim = int(input())
#
# count = 1
# num = 1
#
# while num <= dim:
#     for i in range(count):
#         if num <= dim:
#             print(num, end=' ')
#             num += 1
#         else:
#             break
#     print()
#     count += 1
