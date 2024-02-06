from itertools import product


def truth_tables(tokens):
    # tokens = input()
    lst_tokens = tokens.split()
    variables = [v for v in sorted(set(list(tokens))) if v.isupper()]
    print(*[v for v in variables], 'F')
    length = len(variables)

    def br(tokens):
        if '(' in list(tokens):
            brackets = tokens[tokens.index('('):tokens.index(')') + 1].strip('()').split()
            brackets = translator(brackets)
            res_lst_tokens = tokens[:tokens.index('(')].split()
            res_lst_tokens.append(brackets)
            res_lst_tokens.extend(tokens[tokens.index(')') + 1:].split())
            lst_tokens = res_lst_tokens

    def translator(expression):
        operators = ['not', 'and', 'or', '^', '->', '~']
        for operation in operators:
            if operation in expression:
                match operation:
                    case 'not':
                        for _ in range(expression.count(operation)):
                            index = expression.index(operation)
                            bracket = '(' + expression.pop(index) + ' ' + expression.pop(index) + ')'
                            expression.insert(index, bracket)
                    case 'and' | 'or':
                        for _ in range(expression.count(operation)):
                            index = expression.index(operation)
                            bracket = '(' + expression.pop(index - 1) + ' ' + expression.pop(
                                index - 1) + ' ' + expression.pop(index - 1) + ')'
                            expression.insert(index - 1, bracket)
                    case '^':
                        index = expression.index(operation)
                        a = expression.pop(index - 1)
                        expression.pop(index - 1)
                        b = expression.pop(index - 1)
                        strict_disjunction = ''.join(['(not ' + a + ' and ' + b + ' or ' + a + ' and ' + ' not ', b, ')'])
                        expression.insert(index - 1, strict_disjunction)
                    case '->':
                        index = expression.index(operation)
                        a = expression.pop(index - 1)
                        expression.pop(index - 1)
                        b = expression.pop(index - 1)
                        impl = ''.join(['(', 'not ', a, ' or ', b, ')'])
                        expression.insert(index - 1, impl)
                    case '~':
                        index = expression.index(operation)
                        a = expression.pop(index - 1)
                        expression.pop(index - 1)
                        b = expression.pop(index - 1)
                        equ = ''.join(['(not ' + a + ' and ' + ' not ' + b + ' or ' + a + ' and ' + b + ')'])
                        expression.insert(index - 1, equ)

        res = ''
        for _ in expression:
            res += _
        return res

    if '(' in list(tokens):
        brackets = tokens[tokens.index('('):tokens.index(')') + 1].strip('()').split()
        brackets = translator(brackets)
        res_lst_tokens = tokens[:tokens.index('(')].split()
        res_lst_tokens.append(brackets)
        res_lst_tokens.extend(tokens[tokens.index(')') + 1:].split())
        lst_tokens = res_lst_tokens

    to_eval = translator(lst_tokens)

    for val in product([False, True], repeat=length):
        d = {k: int(v) for k, v in zip(variables, val)}
        print(*[v for v in d.values()], int(eval(to_eval, d)))


def main():
    string = input()
    truth_tables(string)


if __name__ == '__main__':
    main()
# not A or (C ~ not (A -> B) or C)
