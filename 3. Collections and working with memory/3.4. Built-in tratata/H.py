from itertools import islice, cycle

menu_lst = []

for porridge in range(int(input())):
    menu_lst.append(input())

for _ in islice(cycle(menu_lst), int(input())):
    print(_)

# count = 0
# n = int(input())
# while len(res) < n:
#     if count == len(menu_lst):
#         count = 0
#     res.append(menu_lst[count])
#     count += 1
#
# for _ in res:
#     print(_)
