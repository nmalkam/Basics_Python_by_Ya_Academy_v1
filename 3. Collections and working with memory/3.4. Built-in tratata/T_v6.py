"""я хочу решить эту задачу научившись определять выражение в скобочках """
from itertools import product


def truth_tables(tokens):
    # tokens = input()
    lst_tokens = tokens.split()
    variables = [v for v in sorted(set(list(tokens))) if v.isupper()]
    print(*[v for v in variables], 'F')
    length = len(variables)

    def br(tok):
        if '(' in list(tok):
            brack = tok[tok.index('('):tok.index(')') + 1].strip('()').split()
            brack = translator(brack)
            res_lst_tok = tok[:tok.index('(')].split()
            res_lst_tok.append(brack)
            res_lst_tok.extend(tok[tok.index(')') + 1:].split())
            lst_tok = res_lst_tok
            return lst_tok

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
        n = len(lst_tokens)
        for _ in range(lst_tokens.count('(')):
        # for _ in range(len(lst_tokens)):
            if '(' in lst_tokens[n]:
                start_pos = 1


        br(tokens)
    #     brackets = tokens[tokens.index('('):tokens.index(')') + 1].strip('()').split()
    #     brackets = translator(brackets)
    #     res_lst_tokens = tokens[:tokens.index('(')].split()
    #     res_lst_tokens.append(brackets)
    #     res_lst_tokens.extend(tokens[tokens.index(')') + 1:].split())
    #     lst_tokens = res_lst_tokens

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
