from itertools import chain

lst = sorted(chain.from_iterable([input().split(', ') for _ in range(3)]))

for index, value in enumerate(lst, 1):
    print(f'{index}. {value}')


lst = []

for _ in range(3):
    lst.extend(input().split(', '))

for index, value in enumerate(sorted(lst), 1):
    print(f'{index}. {value}')
