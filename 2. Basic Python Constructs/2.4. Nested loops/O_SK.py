# Наивный метод

height = int(input())
width = int(input())

ceil_width = len(str(width * height))

for row in range(height):
    for column in range(width):
        if column % 2 == 0:
            num = column * height + row + 1
        else:
            num = (column + 1) * height - row
        print(f'{num:>{ceil_width}}', end=' ')
    print()
