def NOD(first, second):  # наибольший общий делитель (НОД)
    if first > second:
        bigger = first
        smaller = second
    else:
        bigger = second
        smaller = first
    w_n_l = []  # whole number list
    a = bigger
    while a != 0:
        if bigger % a == 0:
            w_n_l.append(a)
        a -= 1
    while w_n_l:
        if smaller % w_n_l[0] == 0:
            return w_n_l[0]
        w_n_l.remove(w_n_l[0])


assert NOD(12, 42) == 6
assert NOD(512, 625) == 1
# assert NOD(1900, 90000000) == "YES"
# assert NOD(2000) == "YES"
print("Успешно! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    first = int(input())
    second = int(input())
    print(NOD(first, second))


if __name__ == '__main__':
    main()
