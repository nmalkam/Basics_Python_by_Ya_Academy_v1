def my_func(num):
    if num == num[::-1]:
        return 'YES'
    else:
        return 'NO'


assert my_func('1234') == 'NO'
assert my_func('1231234') == 'NO'
assert my_func('123454321') == 'YES'
assert my_func('0') == 'YES'
assert my_func('12344321') == 'YES'
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    num = input()
    print(my_func(num))


if __name__ == '__main__':
    main()
