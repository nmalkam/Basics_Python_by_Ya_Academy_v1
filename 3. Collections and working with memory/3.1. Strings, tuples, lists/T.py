def polish_calculator_2(string: str, factorial=1) -> int:

    tokens = string.split()
    # operators = ['+', '-', '*', '/', ~, !, #, @]
    stack = []

    while tokens != []:
        value = tokens.pop(0)
        if value.isdigit():
            stack.append(int(value))
        else:
            match value:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    stack.append(stack.pop(-2) - stack.pop())
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    stack.append((stack.pop(-2) // stack.pop()))
                case '~':
                    stack.append(stack.pop() * -1)
                case '!':
                    number = stack.pop()
                    for i in range(1, number + 1):
                        factorial *= i
                    stack.append(factorial)
                case '#':
                    cloning = stack.pop()
                    stack.append(cloning)
                    stack.append(cloning)
                case '@':
                    third = stack.pop()
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(second)
                    stack.append(third)
                    stack.append(first)

    # print(stack)
    return stack


# assert polish_calculator_2('410 415 652 710 614 # * + * - /') == [1]
# assert polish_calculator_2('7 1 10 100 #  * @ - + + ~') == -10016
# assert polish_calculator_2('10 15 - 7 *') == -35
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!! ")


def main():

    string = input()

    print(polish_calculator_2(string))


if __name__ == '__main__':
    main()

# возможные ошибки: необходимо правильно поменять знак (~);
# округлять результат от деления;
