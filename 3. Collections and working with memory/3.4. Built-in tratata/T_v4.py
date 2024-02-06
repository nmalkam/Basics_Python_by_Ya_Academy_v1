# КАК РЕАЛИЗОВАТЬ КАЛЬКУЛЯТОР ДЛЯ УРАВНЕНИЙ С НЕСКОЛЬКИМИ СКОБКАИ ВНУТРИ ДРУГ ДРУГА???


# моя задача реализовать правильный порядок, для этого мне нужно добавить скобочки
# из списка очередности я бери операцию, если нахожу, то возвращаю в список преобразованную
# операцию внутри скобочек
# например: было А ор нот В, стало А ор (нот В)
""""""
# A or C ~ not (A -> B) or C
# A -> B ~ C
# (not A and not B) and C
'not A and C ~ not (A -> B) or C'
from itertools import product


def truth_tables():
    def not_standard_translator(expression):
        lst = expression.strip('()').split()
        stack = []
        for index, elem in enumerate(lst):
            if '^' == elem:
                a = lst.pop[index - 1]
                b = lst.pop[index]
                strict_disj = not a and b or a and not b
                stack.append(strict_disj)
        return stack
    # bracket_counter(expression, var, length):
    #     for val in product([True, False], repeat=length):
    #         d = {k: v for k, v in zip(var, )}
    #         int(eval(brackets1, d))

    tokens = input()
    lst_tokens = tokens.split()
    # lst_str = list(tokens)
    # operators = ['not', 'and', 'or', '^', '->', '~', '()']
    flag = 0
    stack = []
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

    # if 'not' in lst_tokens:
    #     for index, elem in enumerate(lst_tokens):
    #         # if 'not' not in elem:
    #         #   stack.append()
    #         if 'not' in elem:
    #             brackets = '(' + lst_tokens.pop(index) + ' ' + lst_tokens.pop(index) + ')'
    #             lst_tokens.insert(index, brackets)

    def translator(expression):
        # lst_tokens = expression.split()
        # expression = ''  # строчка для удаления скобок
        operators = ['not', 'and', 'or', '^', '->', '~']
        for operation in operators:
            # copy_lst_tokens = lst_tokens
            if operation in expression:
                # value = lst_tokens.pop(0)
                match operation:
                    case 'not':
                        for _ in range(expression.count(operation)):
                            index = expression.index(operation)
                            brackets = '(' + expression.pop(index) + ' ' + expression.pop(index) + ')'
                            expression.insert(index, brackets)
                    case 'and' | 'or':
                        for _ in range(expression.count(operation)):
                            index = expression.index(operation)
                            brackets = '(' + expression.pop(index - 1) + ' ' + expression.pop(index - 1) + ' ' + expression.pop(index - 1) + ')'
                            expression.insert(index - 1, brackets)
                        # for index, elem in enumerate(lst_tokens):
                        #     if 'and' in elem:
                        #         brackets = '(' + lst_tokens.pop(index) + ' ' + lst_tokens.pop(index) + ')'
                        #         lst_tokens.insert(index, brackets)
                    case '^':
                        index = expression.index(operation)
                        a = expression.pop(index - 1)
                        # a = a.strip('()')
                        op = expression.pop(index - 1)
                        b = expression.pop(index - 1)
                        # b = b.strip('()')
                        strict_disj = ''.join(['(not ' + a + ' and ' + b + ' or ' + a + ' and ' + ' not ', b, ')'])
                        expression.insert(index - 1, strict_disj)
                    case '->':
                        index = expression.index(operation)
                        a = expression.pop(index - 1)
                        # a = a.strip('()')
                        op = expression.pop(index - 1)
                        b = expression.pop(index - 1)
                        # b = b.strip('()')
                        impl = ''.join(['(', 'not ', a, ' or ', b, ')'])
                        expression.insert(index - 1, impl)
                    case '~':
                        index = expression.index(operation)
                        a = expression.pop(index - 1)
                        # a = a.strip('()')
                        op = expression.pop(index - 1)
                        b = expression.pop(index - 1)
                        # b = b.strip('()')
                        equ = ''.join(['(not ' + a + ' and ' + ' not ' + b + ' or ' + a + ' and ' + b + ')'])  # !!!!!!!!!!!!!!!!!!
                        expression.insert(index - 1, equ)

        res = ''
        for _ in expression:
            res += _
        # res = res.strip('()')
        return res

    if '(' in list(tokens):
        brackets = tokens[tokens.index('('):tokens.index(')') + 1].strip('()').split()
        brackets = translator(brackets)
        # brackets = '(' + brackets + ')'
        res_lst_tokens = tokens[:tokens.index('(')].split()
        res_lst_tokens.append(brackets)
        res_lst_tokens.extend(tokens[tokens.index(')') + 1:].split())
        # ')' воспримет как первую справа или слева, имею в виду что будет в случае двух ')'
        lst_tokens = res_lst_tokens

    to_eval = translator(lst_tokens)
# А КАК Я БУДУ ПЕРЕОПРЕДЕЛЯТЬ ФОРМУЛУ В СКОБКАХ??
# формула в скобках \то просто маленькая формула, я могу вызвать её в программу которая меняет значения
# я думаю это правильный вариант действий!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # while lst_tokens:
    #     value = lst_tokens.pop(0)
    #     if '(' in value:
    #         # index += 1
    #         brackets1.append(value)
    #         flag = 1
    #     elif ')' in value:
    #         brackets1.append(value)
    #         flag = 0
    #         # index -= 1
    #         stack.extend(brackets1)
    #         # stack.append(bracket_counter(brackets1, variables, length))
    #     elif value.isupper():
    #         if flag == 1:
    #             brackets1 += str(value)
    #         else:
    #             stack.append(value)
    #     else:
    #         match value:
    #             case 'not' | 'and' | 'or':
    #                 if flag == 1:
    #                     brackets1.append(value)
    #                 else:
    #                     stack.append(value)
    #             case '^':
    #                 a = stack.pop()
    #                 b = lst_tokens.pop(0)
    #                 strict_disj = not a and b or a and not b
    #                 if flag == 1:
    #                     brackets1.append(strict_disj)
    #                 else:
    #                     stack.append(strict_disj)
    #             case '->':
    #                 a = stack.pop()
    #                 b = lst_tokens.pop(0)
    #                 impl = not a or b
    #                 if flag == 1:
    #                     brackets1.append(impl)
    #                 else:
    #                     stack.append(impl)
    #             case '~':
    #                 a = stack.pop()
    #                 b = lst_tokens.pop(0)
    #                 equ = not a and not b or a and b
    #                 if flag == 1:
    #                     brackets1.append(equ)
    #                 else:
    #                     stack.append(equ)
    for val in product([False, True], repeat=length):
        d = {k: int(v) for k, v in zip(variables, val)}
        print(*[v for v in d.values()], int(eval(to_eval, d)))  # ' '.join(to_eval), d)))
        # надо обязательно решить () потому что я не могу подать значение справа,
        # ибо сначала нужно решить то что в скобках


truth_tables()
# ещё есть вариант когда у меня несколько списков и я иду просто слева на право
# и в разные списки в зависимости от порядка операции вношу в списки переменные,
# но идея так себе
