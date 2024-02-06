# not A or (C ~ not (A -> B) or C)
s = 'not A or (C ~ not (A -> B) or C)'

operators = ['not', 'and', 'or', '^', '->', '~']
variables = [v for v in sorted(set(list(s))) if v.isupper()]
# print()
a = s.strip(f'{variables}{operators} ')
print(a)
