def no_comments_2():
    from sys import stdin
    for line in stdin:
        # print(line.rstrip('\n'))
        # print(list(line.rstrip('\n')))
        lst_line = list(line.rstrip('\n'))
        # l =
        if '#' == lst_line[0]:
            continue
        elif '#' in list(line.rstrip('\n')):
            print(''.join(lst_line[:lst_line.index('#')]))
        else:
            print(line)


def main():
    no_comments_2()


if __name__ == '__main__':
    main()

# def no_comments():
#     while (string := input()) != '':
#         find = 0
#         if string[0] == '#':
#             continue
#         for letter in string:
#             if letter == '#':
#                 if string[:int(string.index('#'))] == ' ':
#                     print(string[:int(string.index('#'))])
#                     find = 1
#                     break
#                 else:
#                     print(string[:int(string.index('#'))])
#                     find = 1
#                     break
#         if find == 0:
#             print(string)
