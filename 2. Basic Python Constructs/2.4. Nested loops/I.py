# max(hash, key=hash.get)
# max(hash.values())
def big_number():
    n = int(input())
    count = 0
    res = ''
    max_num = 0
    while count != n:
        num = input()
        for i in str(num):
            if int(max_num) < int(i):
                max_num = i
        res = res + max_num
        count += 1
        max_num = 0
    return int(res)

# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    print(big_number())


if __name__ == '__main__':
    main()
