def private_property():

    toys_lst = []
    res = []

    for num in range(n := int(input())):
        toys_lst.extend(list(set((input().replace(',', '').split())[1:])))

    for word in range(len(toys_lst)):
        x = toys_lst.pop(0)
        if x not in toys_lst:
            res.append(x)
        toys_lst.append(x)
    for _ in sorted(res):
        print(_)

# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():

    private_property()


if __name__ == '__main__':
    main()
