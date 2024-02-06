def polish_calculator(string: str) -> int:

    arithmetic = 0
    list_string = string.split()
    stack = []

    for _ in list_string:
        if _.isdigit():
            stack.append(_)
        else:
            match _:
                case '+':
                    arithmetic = int(stack.pop()) + int(stack.pop())
                case '-':
                    subtrahend = int(stack.pop())  # вычитаемое
                    minuend = int(stack.pop())  # уменьшаемое
                    arithmetic = minuend - subtrahend
                case '*':
                    arithmetic = int(stack.pop()) * int(stack.pop())
                case '/':
                    divisor = int(stack.pop())  # делитель
                    dividend = int(stack.pop())  # делимое
                    arithmetic = dividend / divisor
            stack.append(arithmetic)
    return stack[0]


assert polish_calculator('7 2 3 * -') == 1
assert polish_calculator('10 15 - 7 *') == -35
# assert polish_calculator(8, 0) == "Вы вышли в море и рискуете быть съеденным акулой!"
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    string = input()
    print(polish_calculator(string))


if __name__ == '__main__':
    main()

# моя первая версия
# while index != len(stack):
    #     if stack[index].isdigit():
    #         now = eval(f'{stack[index - 2]}{stack[index]}{stack[index - 1]}')
    #         # print(now)
    #         # print(type(now))
    #         stack[(index - 2):index + 1] = [str(now)]
    #         index = 0
    #     elif len(stack) == 1:
    #         print(stack[0])
    #         return stack[0]
    #     else:
    #         index += 1
