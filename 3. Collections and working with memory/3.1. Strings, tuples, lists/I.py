# Задача I
# Без комментариев
#
# Ну есть же правила
#
# два пробела перед '#'
#
# Вы не принимаете решение если я не ставлю два пробела по правилам
#
# вы не принимаете задачу если я логически удаляю два пробела(даже 1, как в примере)
#
# ?????
#
# Profit!

def no_comments():
    while (string := input()) != '':
        find = 0
        if string[0] == '#':
            continue
        for letter in string:
            if letter == '#':
                if string[:int(string.index('#'))] == ' ':
                    print(string[:int(string.index('#'))])
                    find = 1
                    break
                else:
                    print(string[:int(string.index('#'))])
                    find = 1
                    break
        if find == 0:
            print(string)


def main():
    no_comments()


if __name__ == '__main__':
    main()
