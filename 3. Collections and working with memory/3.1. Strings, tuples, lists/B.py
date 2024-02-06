# from typing import Optional


def twist_turn(string: str = None):  # -> Optional[str]:
    for letter in string:
        print(letter)


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    string = input()
    twist_turn(string)


if __name__ == '__main__':
    main()
