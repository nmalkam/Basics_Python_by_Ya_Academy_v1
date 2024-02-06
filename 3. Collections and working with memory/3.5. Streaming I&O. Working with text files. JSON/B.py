from sys import stdin


def average_height():
    height = []
    for line in stdin:
        elements = line.split()
        h = int(elements[2]) - int(elements[1])
        height.append(h)
    n = len(height)
    res = sum(height) / n
    return round(res)


# print("Успешное выполнение оператора assert")


def main():
    print(average_height())


if __name__ == '__main__':
    main()
