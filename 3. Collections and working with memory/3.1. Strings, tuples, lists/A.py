from typing import Optional


def alphabet() -> Optional[str]:  # hornbook
    count = 0
    n = int(input())
    while count != n:
        word = input()
        if not (word.startswith('а') or word.startswith('б') or word.startswith('в')):
            return 'NO'
        count += 1
    return 'YES'


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    print(alphabet())


if __name__ == '__main__':
    main()
