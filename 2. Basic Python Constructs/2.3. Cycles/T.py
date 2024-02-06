def Blockchain():
    # Block bn with number n, includes information mn(natural number), rn-random number9(from 0 to 255)
    # hn hash(целое число{from 0 to 255})
    import random
    blocks = int(input())
    list_blocks_given = []
    enterings = 0
    h_list_blocks_given = [0]
    while enterings != blocks:  # input
        list_blocks_given.append(int(input()))
        enterings += 1

    index_h = 1
    index_b = 0
    for block in list_blocks_given:
        mn = random.randint(0, 255)
        rn = random.randint(0, 255)  # постоянные или нет??
        hn = (37 * (mn + rn + h_list_blocks_given[index_h - 1])) % 256
        h_list_blocks_given.append(hn)
        if hn >= 100 or hn + rn != (block / (256 + mn * 256 ** 2)):  # bn = hn + rn * 256 + mn * 256**2
            print(hn)
            print(hn + rn)
            print((256 + mn * 256 ** 2))
            return index_b + 1  # или просто index_b???
        index_b += 1
    print(-1)


print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    print(Blockchain())


if __name__ == '__main__':
    main()
