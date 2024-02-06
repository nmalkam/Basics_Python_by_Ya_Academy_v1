def data_cleaning():
    while (string := input()) != '':
        if string.endswith('@@@'):
            pass
        elif string.startswith('##'):
            print(string[2:])
        else:
            print(string)


# assert data_cleaning() == "Петя"
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    data_cleaning()


if __name__ == '__main__':
    main()
