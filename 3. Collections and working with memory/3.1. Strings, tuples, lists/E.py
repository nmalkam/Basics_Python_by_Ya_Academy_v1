def rose_of_Azor_4(string: str) -> str:  # 2.2. G
    reversed = string[::-1]
    if string == reversed:
        return "YES"
    else:
        return "NO"


assert rose_of_Azor_4('мама') == 'NO'
assert rose_of_Azor_4('анна') == 'YES'
# print("Успешное выполнение оператора assert")


def main():
    string = input()
    print(rose_of_Azor_4(string))


if __name__ == '__main__':
    main()
