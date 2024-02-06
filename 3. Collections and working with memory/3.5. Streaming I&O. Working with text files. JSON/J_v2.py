"""скользящее окно"""
file_in = 'first.txt'
n = 2
# file_in = input()
# n = input()
res = []
with open(file_in, 'r', encoding="UTF-8") as file_in:
    for line in file_in.readlines():
        res.append(line)
        if len(res) > n:
            res.pop(0)
    # for item in res:
    #     print(item, end='')
    print(''.join(res), end='')

