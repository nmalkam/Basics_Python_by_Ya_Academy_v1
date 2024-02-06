def friends_of_friends():
    subjects = set()  # множество имен
    friends = {}  # словарь прямых друзей

    while pair := input():
        friend1, friend2 = pair.split()
        friends[friend1] = friends.get(friend1, set()) | set([friend2])
        friends[friend2] = friends.get(friend2, set()) | set([friend1])

    friends_of_friends = {}  # словарь друзей друзей

    for name in sorted(friends):
        for person in friends[name]:
            friends_of_friends[name] = friends_of_friends.get(name, set()) | friends[person]

    for name in friends_of_friends:
        friends_of_friends[name].discard(name)  # удаляем самого себя
        for friend in friends[name]:  # удаляем прямых друзей
            friends_of_friends[name].discard(friend)

        friends_of_friends[name] = sorted(friends_of_friends[name])

        print(f'{name}: {", ".join(friends_of_friends[name])}')


def main():

    friends_of_friends()


if __name__ == '__main__':
    main()
