def everything_found_2():
    list = []
    for _ in range(3):
        list.append(input())
    # from sys import stdin
    #
    # lines = stdin.readlines()
    subject = list[-1].strip('\n').lower()
    objects = list[:-1]

    for line in objects:
        if line.lower().find(subject) + 1:
            print(line.strip('\n'))

    # from sys import stdin
    # lst = []
    # for line in stdin:
    #     lst.append(line.rstrip('\n'))
    # query = lst.pop(-1)
    # for elem in lst:
    #     if query in elem.lower():
    #         print(elem)


def main():
    everything_found_2()


if __name__ == '__main__':
    main()
