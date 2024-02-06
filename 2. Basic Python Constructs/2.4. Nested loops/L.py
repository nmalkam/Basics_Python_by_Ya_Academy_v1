def number_rectangle(height: int, width: int):

    cell_width = len(str(width * height))

    pos = 1
    number = 1

    for _ in range(height):
        for _ in range(width):
            if pos == width:
                print(f'{number:>{cell_width}}')
                pos = 1
            else:
                print(f'{number:>{cell_width}}', end=' ')
                pos += 1
            number += 1


# assert number_rectangle(3, 4) == 1
# assert number_rectangle(2, 3) == 1
# assert number_rectangle(4, 6) == 1
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    width = int(input())
    height = int(input())
    number_rectangle(width, height)


if __name__ == '__main__':
    main()
