def number_rectangle(n, m):

    count = 1
    num = 1

    while num <= n * m:
        for i in range(m):
            if num <= m:
                print(num, end=' ')
                num += 1
            else:
                break
        print()
        count += 1


assert number_rectangle(3, 4) == 1
# assert number_rectangle(2, 3) == 1
# assert number_rectangle(4, 6) == 1
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    n = int(input())
    m = int(input())
    number_rectangle(n, m)


if __name__ == '__main__':
    main()




# def number_rectangle(n, m):
#
#     num = 1
#     pos_raw = 1
#     # first_in_row = ' '
#     # first_nine = ' '
#     if m * n >= 10:  # and :
#         space = ' '
#     else:
#         space = ''
#
#     for i in range(n):
#         for j in range(m):
#             if num // 10 == 0:  # and pos_raw == 1 or num // 10 == 0 and pos_raw != 1:
#                 print(f'{space}{num}', end=' ')
#             # elif num // 10 == 0 and pos_raw != 1:
#             #     print(f'{first_nine}{num}', end=' ')
#             else:
#                 print(num, end=' ')
#             num += 1
#             if pos_raw == m:
#                 print()
#                 pos_raw = 1
#             else:
#                 pos_raw += 1
#         # else:
#         #     for i in range(n):
#         #         for j in range(m):
#         #             print(num, end=' ')
#         #             num += 1
#         #             if pos_raw == m:
#         #                 print()
#         #                 pos_raw = 1
#         #             else:
#         #                 pos_raw += 1
#
#
# # assert number_rectangle(3, 4) == 1
# # assert number_rectangle(2, 3) == 1
# # assert number_rectangle(4, 6) == 1
# # print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")
#
#
# def main():
#     n = int(input())
#     m = int(input())
#     number_rectangle(n, m)
#
#
# if __name__ == '__main__':
#     main()
#
# #  1  2  3  4  5  6
# #  7  8  9 10 11 12
# # 13 14 15 16 17 18
# # 19 20 21 22 23 24
