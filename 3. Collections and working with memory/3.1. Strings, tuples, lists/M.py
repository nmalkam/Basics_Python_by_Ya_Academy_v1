def mass_exponentiation():

    nums = []
    n = int(input())

    while len(nums) != n:
        nums.append(int(input()))

    power = int(input())

    for _ in nums:
        print(_ ** power)


# assert mass_exponentiation() == 1
# assert mass_exponentiation() == 1
# assert mass_exponentiation() == 1
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    mass_exponentiation()


if __name__ == '__main__':
    main()
