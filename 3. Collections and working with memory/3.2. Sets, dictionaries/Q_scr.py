def friends_of_friends():

    d_rib = {}
    d_2_level = {}

    while (rib := input()) != '':
        a_rib, b_rib = map(str, rib.split())
        d_rib[a_rib] = d_rib.get(a_rib, []) + [b_rib]
        d_rib[b_rib] = d_rib.get(b_rib, []) + [a_rib]

    for key in sorted(d_rib.keys()):
        val = set()
        for name in d_rib[key]:
            val = set(d_rib[name]) - {key}
        d_2_level[key] = d_2_level.get(key, []) + sorted(val)

    for key in sorted(d_2_level.keys()):
        print(f'{key}: {sorted(d_2_level[key])}')
    print()


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():

    friends_of_friends()


if __name__ == '__main__':
    main()
