def rose_of_Azor_5(string: str) -> str:  # 2.2. G   ->   3.1 E  А роза упала на лапу Азора 4.0
    reversed = string.lower().replace(' ', '')[::-1]
    if string.lower().replace(' ', '') == reversed:
        return "YES"
    else:
        return "NO"


assert rose_of_Azor_5('Мама мыла раму') == 'NO'
assert rose_of_Azor_5('А роза упала на лапу Азора') == 'YES'
# print("Успешное выполнение оператора assert")


def main():
    string = input()
    print(rose_of_Azor_5(string))


if __name__ == '__main__':
    main()
