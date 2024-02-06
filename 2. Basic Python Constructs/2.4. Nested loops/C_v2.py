# не дописал. исправил v1 и добавил костылей

def christmas_mood(n):
    count = 1
    columns = 1
    raws = 1
    res = ''
    for i in range(n + 1):
        while columns != i + 1:
            for j in range(raws + 1):
                res += ' ' + str(count)
                count += 1
            print(res)
            raws += 1
        columns += 1




# assert christmas_mood(1) == '1'
# assert christmas_mood(10) == '1'
# assert christmas_mood(2) == '1\n2'
# assert christmas_mood(3) == '1, \n, 2, 3'
assert christmas_mood(6) == '1\n2 3\n4 5 6'
# assert christmas_mood(14) == '1\n2 3\n4 5 67 8 9 1011 12 13 14'


def main():
    n = int(input())
    christmas_mood(n)


if __name__ == '__main__':
    main()
