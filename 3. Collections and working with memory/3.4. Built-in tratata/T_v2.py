# КАК РЕАЛИЗОВАТЬ КАЛЬКУЛЯТОР ДЛЯ УРАВНЕНИЙ С НЕСКОЛЬКИМИ СКОБКАИ ВНУТРИ ДРУГ ДРУГА???


# моя задача реализовать правильный порядок, для этого мне нужно добавить скобочки
# из списка очередности я бери операцию, если нахожу, то возвращаю в список преобразованную
# операцию внутри скобочек
# например: было А ор нот В, стало А ор (нот В)
# A or C ~ not (A -> B) or C
# A -> B ~ C
# (not A and not B) and C
from itertools import product
def truth_tables():
    # def bracket_counter(expression, var, length):
    #     for val in product([True, False], repeat=length):
    #         d = {k: v for k, v in zip(var, )}
    #         int(eval(brackets1, d))

    tokens = input()
    lst_tokens = tokens.split()
    # lst_str = list(tokens)
    # operators = ['not', 'and', 'or', '^', '->', '~', '()']
    stack = []
    flag = 0
    brackets1 = []
    # brackets2 = []
    # brackets3 = []
    # если "(" есть в now то list(now) и добавить в новый список пока не дойдем до ")" добавляем всё в список
    # как нашли ")" добавили в список, после eval список,
    # но что делать если "((A or B) not C and A)"
    # нужно попробовать передать () в eval, по идее он должен отработать
    # index = 0
    variables = [v for v in sorted(set(list(tokens))) if v.isupper()]  # можно заменить lst_str
    print(*[v for v in variables], 'F')
    length = len(variables)
    while lst_tokens:
        value = lst_tokens.pop(0)
        if '(' in value:
            # index += 1
            brackets1.append(value)
            flag = 1
        elif ')' in value:
            brackets1.append(value)
            flag = 0
            # index -= 1
            stack.extend(brackets1)
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
                        brackets1.append(value)
                    else:
                        stack.append(value)
                case '^':
                    a = stack.pop()
                    b = lst_tokens.pop(0)
                    strict_disj = not a and b or a and not b
                    if flag == 1:
                        brackets1.append(strict_disj)
                    else:
                        stack.append(strict_disj)
                case '->':
                    a = stack.pop()
                    b = lst_tokens.pop(0)
                    impl = not a or b
                    if flag == 1:
                        brackets1.append(impl)
                    else:
                        stack.append(impl)
                case '~':
                    a = stack.pop()
                    b = lst_tokens.pop(0)
                    equ = not a and not b or a and b
                    if flag == 1:
                        brackets1.append(equ)
                    else:
                        stack.append(equ)
    for val in product([False, True], repeat=length):
        d = {k: int(v) for k, v in zip(variables, val)}
        print(*[v for v in d.values()], int(eval(' '.join(stack), d)))
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
truth_tables()
