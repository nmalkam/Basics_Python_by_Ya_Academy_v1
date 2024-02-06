# Полное решение
from typing import Optional


def christmas_mood(num: int):  # -> Optional[str]:
    # num = int(input())
    count = 1
    ranged = 2
    list_j = []
    # if num == 1:
    #     print(1)
    # elif num == 2:
    #     print('1\n2')
    #     return
    # for i in range(1, num):
        # if count == num + 1:
        #     break
    while count != num + 1:
        for j in range(1, ranged):
            if count != num + 1:
                list_j.append(str(count))
                count += 1
        result = ' '.join(list_j)
        print(result)
        list_j = []
        ranged += 1


# assert christmas_mood(1) == '1'
# assert christmas_mood(10) == '1'
# assert christmas_mood(2) == '1\n2'
# assert christmas_mood(3) == '1, \n, 2, 3'
# assert christmas_mood(6) == '1\n2 3\n4 5 6'
# assert christmas_mood(14) == '1\n2 3\n4 5 67 8 9 1011 12 13 14'


def main():
    num = int(input())
    christmas_mood(num)


if __name__ == '__main__':
    main()
