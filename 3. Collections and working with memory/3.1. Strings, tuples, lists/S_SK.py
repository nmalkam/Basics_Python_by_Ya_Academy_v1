def polish_calculator(string):

    tokens = string.split(' ')

    # operators = ['+', '-', '*', '/']
    stack = []

    while tokens:
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
                    stack.append(stack.pop(-2) / stack.pop())
    return stack[0]


assert polish_calculator('7 2 3 * -') == 1
# assert polish_calculator('10 15 - 7 *') == -35
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():

    string = input()

    print(polish_calculator(string))


if __name__ == '__main__':
    main()
