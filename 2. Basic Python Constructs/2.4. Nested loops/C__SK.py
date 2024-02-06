# Решение с вложенными циклами

# dim = int(input())
#
# count = 1
# num = 1
#
# while num <= dim:
#     for i in range(count):
#         if num <= dim:
#             print(num, end=' ')
#             num += 1
#         else:
#             break
#     print()
#     count += 1

# Решение с одни циклом

dim = int(input())

num = 1
pos = 1

for i in range(dim):
    print(i + 1, end=' ')
    if pos == num:
        print()
        pos = 1
        num += 1
    else:
        pos += 1
