def polish_calculator(string):

    token = string.split()
    stack = []
    index = 0

    while len(token) != 0:
        if token[0] ==
        stack.append(token[index])




assert polish_calculator('7 2 3 * -') == "1"
assert polish_calculator('10 15 - 7 *') == '-35'
# assert polish_calculator(8, 0) == "Вы вышли в море и рискуете быть съеденным акулой!"
print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    string = input()
    print(polish_calculator(string))


if __name__ == '__main__':
    main()
