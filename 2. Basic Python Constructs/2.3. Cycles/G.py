def NOK(first, second):
    if first > second:
        bigger = first
        smaller = second
    else:
        bigger = second
        smaller = first
    b_c_l = []  # bigger_consist_list
    s_c_l = []  # smaller_consist_list
    divided_bigger = bigger
    divided_smaller = smaller
    while divided_bigger != 1:
        for number in range(2, (divided_bigger + 1)):
            if divided_bigger % number == 0:
                b_c_l.append(number)
                divided_bigger = int(divided_bigger / number)
                break
        # if divided_bigger == 1:
        #     break
        # else:
        #     number = 2
        #     continue
    while divided_smaller != 1:
        for number in range(2, (divided_smaller + 1)):
            if divided_smaller % number == 0:
                s_c_l.append(number)
                divided_smaller = int(divided_smaller / number)
                break
        # if divided_bigger == 1:
        #     break
        # else:
        #     number = 2
        #     continue
    coincidences_list = list(set(b_c_l) & set(s_c_l))
    nok = 1
    for item in coincidences_list:
        nok = item * nok
    b_c_l_set = set(b_c_l)
    s_c_l_set = set(s_c_l)
    common_values = b_c_l_set.intersection(s_c_l_set)
    for value in common_values:
        b_c_l.remove(value)
        s_c_l.remove(value)
    difference_list = b_c_l + s_c_l
    for iiitem in difference_list:
        nok = iiitem * nok
    return nok


assert NOK(12, 42) == 84
assert NOK(100, 10) == 100
assert NOK(512, 625) == 320000
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    # first, second = map(int, input().split())
    first = int(input())
    second = int(input())
    print(NOK(first, second))


if __name__ == '__main__':
    main()
# (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31...)
