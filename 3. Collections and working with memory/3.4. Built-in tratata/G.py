from itertools import combinations

# lst_names = list(combinations([input() for name in range(int(input()))], 2))
for f, s in list(combinations([input() for name in range(int(input()))], 2)):
    print(f'{f} - {s}')
