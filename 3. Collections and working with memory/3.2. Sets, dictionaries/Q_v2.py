# мне нужен список всех друзей key потом список друзей друзей
# из списка друзей друзей я вычитаю друзей и сам key
def friends_of_friends():

    d_rib = {}
    d_2_level = {}

    while (rib := input()) != '':
        a_rib, b_rib = rib.split()
        d_rib[a_rib] = d_rib.get(a_rib, []) + [b_rib]
        d_rib[b_rib] = d_rib.get(b_rib, []) + [a_rib]

    for key in sorted(d_rib.keys()):
        val = set()
        for name in d_rib[key]:
            friend_of_friends = set(d_rib[name]) - {key} | val
            val = friend_of_friends - set(d_rib[key])
        d_2_level[key] = d_2_level.get(key, []) + sorted(val)

    for key in d_2_level.keys():
        print(key, end=': ')
        res = ''
        for v in d_2_level[key]:
            res += v + ', '
        print(res[:-2])


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():

    friends_of_friends()


if __name__ == '__main__':
    main()
