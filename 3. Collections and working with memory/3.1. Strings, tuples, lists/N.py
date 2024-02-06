def mass_exponentiation_2(list_nums, power):

    num = list_nums.split(' ')
    for _ in num:
        print(int(_) ** power, end=' ')
        # if num


# assert mass_exponentiation_2('2 3 4', 3) == '8 27 64'
# assert mass_exponentiation_2('222222 22222 2222 222 22', 2) == '49382617284 493817284 4937284 49284 484'
# assert mass_exponentiation_2() == 1
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():

    list_nums = input()
    power = int(input())

    mass_exponentiation_2(list_nums, power)


if __name__ == '__main__':
    main()
