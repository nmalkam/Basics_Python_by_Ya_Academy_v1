def simple_num(num):
    k = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            k = k + 1
    if k <= 0:
        return 'YES'
    else:
        return 'NO'


assert simple_num(6) == "NO"
assert simple_num(909999999) == "YES"
assert simple_num(67) == "YES"
print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    num = int(input())
    print(simple_num(num))


if __name__ == '__main__':
    main()
