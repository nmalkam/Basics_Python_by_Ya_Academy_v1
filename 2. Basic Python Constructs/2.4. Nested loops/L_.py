# для решения этой задачи нужно знать форматирование строки


# например format()


# если уметь указывать длину выводимого символа,
# то будет достаточно одного пробела после вывода.
# потому как в выводе уже будет необходимый пробел(если необходим,
# в случае вывода однозначного числа)


# f'{(number):>{cell_width}}', end=' ')   cell_width = len(str(height * width))


from typing import Optional


def number_rectangle(n: int, m: int) -> Optional[list]:
    return [1, 2, 3]


assert number_rectangle(2, 3) == 1
assert number_rectangle(4, 6) == 1
print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    n, m = [int(input()) for _ in range(2)]
    print(number_rectangle(n, m))


if __name__ == '__main__':
    main()
