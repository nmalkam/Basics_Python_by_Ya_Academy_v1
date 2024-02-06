def treasure_map() -> int:

    coord = []
    d = {}

    for num in range(int(input())):
        x, y = map(int, input().split())
        coord.append(x)
        d[f'{x // 10};{y // 10}'] = d.get(f'{x // 10};{y // 10}', 0) + 1

    # print(max(d.values()))
    return max(d.values())


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    print(treasure_map())


if __name__ == '__main__':
    main()
