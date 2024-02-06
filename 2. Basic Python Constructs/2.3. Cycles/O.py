def zaika4():
    # print('березка зайка'.find('зайка'))
    n = int(input())
    count = 0
    z = 0
    while count != n:
        for item in (row := input().split(' ')):
            if 'зайка' in item:
                z += 1
                break
        count += 1
    return z


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    print(zaika4())


if __name__ == '__main__':
    main()
