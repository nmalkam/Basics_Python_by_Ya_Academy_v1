max_symb = int(input()) - 3
line = int(input())
list = []
for i in range(line):
    list.append(input())

count_symb = 0

for elem in list:
    if len(elem) + count_symb < max_symb:
        print(elem)
        count_symb += len(elem)
    else:
        print(elem[:max_symb - count_symb] + '...')
        break
