def ORANGE(segment):
    print('А Б В')
    n_list = []
    for a in range(1, segment):
        for b in range(1, segment):
            for v in range(1, segment):
                if a + b + v == segment:
                    n_list.append([a, b, v])
                    # n_list.append(str(a) + ' ' + str(b) + ' ' + str(v))
    # print(sorted(n_list))
    # return sorted(n_list)
    result = ''
    for item in sorted(n_list):
        for num in item:
            result += str(num) + ' '
        print(result[:-1])
        result = ''


# assert ORANGE(600) == ["1 1 1"]
assert ORANGE(100) == ["1 1 1"]
assert ORANGE(3) == ["1 1 1"]
assert ORANGE(5) == ["1 1 3", "1 2 2", "1 3 1", "2 1 2", "2 2 1", "3 1 1"]
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    segment = int(input())
    ORANGE(segment)


if __name__ == '__main__':
    main()
