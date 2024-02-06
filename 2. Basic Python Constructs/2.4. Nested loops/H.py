# max(hash, key=hash.get)
# max(hash.values())
def maximum_amount():
    n = int(input())
    count = 0
    # result = ''
    hash = {}
    while count != n:
        result = 0
        name = input()
        num = input()
        for i in str(num):
            result += int(i)
            hash[name] = result
        count += 1
    target_grade = max(hash.values())
    winners = []  # [key for key in hash if hash[key] == target_grade]
    for key, value in hash.items():
        if value == target_grade:
            winners.append(key)
    return winners[-1]

# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    print(maximum_amount())


if __name__ == '__main__':
    main()
