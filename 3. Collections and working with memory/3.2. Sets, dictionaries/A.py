# однострочник
# print(''.join(set(input())))


def symbolic_squeeze(word: str) -> str:

    set_sum = ''

    for _ in set(word):
        set_sum += _
    return set_sum


assert symbolic_squeeze('змееед') == 'здме'
assert symbolic_squeeze('велосипед') == 'исолвдеп'
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():

    word = input()

    print(symbolic_squeeze(word))


if __name__ == '__main__':
    main()
