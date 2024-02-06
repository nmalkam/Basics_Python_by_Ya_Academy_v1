def christmas_mood_2(num: int):

    list_result = []
    len_raw = []
    count = 1
    ranged = 2
    list_j = []

    if num == 1:
        print(1)
        return
    elif num == 2:
        print('1\n2')
        return
    for i in range(1, num):
        if count == num + 1:
            break
        for j in range(1, ranged):
            if count != num + 1:
                list_j.append(str(count))
                count += 1
        result = ' '.join(list_j)
        list_result.append(result)
        list_j = []
        ranged += 1
        len_raw.append(len(result))
    for item in list_result:
        print(f'{item:^{max(len_raw)}}')


# assert christmas_mood_2(1) == '1'
# assert christmas_mood_2(10) == '1'
# assert christmas_mood_2(2) == '1\n2'
# assert christmas_mood_2(3) == '1, \n, 2, 3'
# assert christmas_mood_2(6) == '1\n2 3\n4 5 6'
# assert christmas_mood_2(14) == '1\n2 3\n4 5 67 8 9 1011 12 13 14'
# assert christmas_mood_2(8) == '1\n2 3\n4 5 67 8 9 1011 12 13 14'


def main():
    num = int(input())
    christmas_mood_2(num)


if __name__ == '__main__':
    main()
