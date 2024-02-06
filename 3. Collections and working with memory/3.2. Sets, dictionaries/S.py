def private_property():

    toys_lst = 1
    lst_sets = []
    res = []
    d_kids = {}
    d_toys = {}

    for num in range(n := int(input())):
        # s = input().split()
        lst_sets.append(set((input().replace(',', '').split())[1:]))
        # d_kids[s[0]] = s[1:]

    for st, index in enumerate(lst_sets):
        res = st
        reminder = st
        for num in range(n):
            cop_lst_sets = lst_sets[:]
            res -= lst_sets[num]
    print()


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():

    private_property()


if __name__ == '__main__':
    main()
