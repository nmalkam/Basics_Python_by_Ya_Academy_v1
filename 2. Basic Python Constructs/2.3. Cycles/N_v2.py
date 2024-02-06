def simple_num(num):
    q = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 51, 53, 57, 59, 61]
    # if num
    item_list = []
    for item in range(1, num + 1):
        if num % item == 0:
            item_list.append(item)
    # print(len(item_list))
    # print(item_list)
    if (len(item_list) == 2) and (1 and num in item_list):
        return 'YES'
    else:
        return 'NO'
# 3761 3767 3769 3779 260003 260009 260011 260017 260023
# 260047 260081 260089 260111 20999999 20999999


assert simple_num(6) == "NO"
print(12345)
assert simple_num(909999999) == "YES"
assert simple_num(67) == "YES"
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    num = int(input())
    print(simple_num(num))


if __name__ == '__main__':
    main()

# sum(int(digit) for digit in input())
# sum(map(int, input()))
