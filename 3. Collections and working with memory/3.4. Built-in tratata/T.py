# неправильная версию с переводом в строку


# КАК РЕАЛИЗОВАТЬ КАЛЬКУЛЯТОР ДЛЯ УРАВНЕНИЙ С НЕСКОЛЬКИМИ СКОБКАИ ВНУТРИ ДРУГ ДРУГА???
# A or C ~ not (A -> B) or C
# A -> B ~ C
# (not A and not B) and C
from itertools import product
def truth_tables():
    def bracket_counter(expression, var, length):
        for val in product([True, False], repeat=length):
            d = {k: v for k, v in zip(var, )}
            int(eval(brackets1, d))

    tokens = input()
    lst_tokens = tokens.split()
    lst_str = list(tokens)
    # operators = ['not', 'and', 'or', '^', '->', '~', '()']
    stack = []
    flag = 0
    brackets1 = ''
    # brackets2 = []
    # brackets3 = []
    # если "(" есть в now то list(now) и добавить в новый список пока не дойдем до ")" добавляем всё в список
    # как нашли ")" добавили в список, после eval список,
    # но что делать если "((A or B) not C and A)"
    # нужно попробовать передать () в eval, по идее он должен отработать
    # index = 0
    variables = [v for v in sorted(set(lst_str)) if v.isupper()]  # можно заменить lst_str
    length = len(variables)
    while lst_tokens:
        value = lst_tokens.pop(0)
        if '(' in value:
            # index += 1
            brackets1 += str(value)
            flag = 1
        if ')' in value:
            brackets1 += str(value)
            flag = 0
            # index -= 1
            stack.append(brackets1)
            # stack.append(bracket_counter(brackets1, variables, length))
        elif value.isupper():
            if flag == 1:
                brackets1 += str(value)
            else:
                stack.append(value)
        else:
            match value:
                case 'not' | 'and' | 'or':
                    if flag == 1:
                        brackets1 += str(value)
                    else:
                        stack.append(value)
                # operators = ['^', '->', '~']
                case '^':  # | '->' | '~':
                    if flag == 1:
                        brackets1
                    else:
                        stack.append(value)  # CHECK!!!!!

                    left = stack.pop()
                    # right =
                    stack.append(stack.pop() * stack.pop())
                # надо обязательно решить () потому что я не могу подать значение справа,
                # ибо сначала нужно решить то что в скобках
                # case '/':
                #     stack.append((stack.pop(-2) // stack.pop()))
                # case '~':
                #     stack.append(stack.pop() * -1)
                # case '!':
                #     number = stack.pop()
                #     factorial = 1
                #     for i in range(1, number + 1):
                #         factorial *= i
                #     stack.append(factorial)
                # case '#':
                #     cloning = stack.pop()
                #     stack.append(cloning)
                #     stack.append(cloning)
                # case '@':
                #     third = stack.pop()
                #     second = stack.pop()
                #     first = stack.pop()
                #     stack.append(second)
                #     stack.append(third)
                #     stack.append(first)

# assert truth_tables('A -> B ~ C') == 1
# assert truth_tables('A or C ~ not (A -> B) or C') == 1

# возможные ошибки: необходимо правильно поменять знак (~);
# округлять результат от деления;
