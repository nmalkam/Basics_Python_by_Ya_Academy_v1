from sys import stdin


def average_height():
    height = 0
    n = 0
    for line in stdin:
        elements = line.split()
        h = int(elements[2]) - int(elements[1])
        height += h
        n += 1
    return round(height / n)


# print("Успешное выполнение оператора assert")


def main():
    print(average_height())


if __name__ == '__main__':
    main()
