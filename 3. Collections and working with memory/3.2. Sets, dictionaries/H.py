def porridge_eater_4():

    d = {}
    flag = 0
    alp_surname_lst = []

    for _ in range(int(input())):
        strng = input().split()
        d[strng[0]] = strng[1:]

    choice = input()

    for key, val in d.items():
        if choice in val:
            alp_surname_lst.append(key)
            flag = 1
    for surname in sorted(alp_surname_lst):
        print(surname)
    if flag == 0:
        print('Таких нет')


def main():
    porridge_eater_4()


if __name__ == '__main__':
    main()
