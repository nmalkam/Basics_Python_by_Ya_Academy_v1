def simple_task_4():

    numbers = list(set(input().split('; ')))

    numbers = sorted(set([int(number) for number in numbers]))

    for num1 in numbers:
        gcd = []
        for num2 in numbers:
            if num1 - num2:
                a, b = num1, num2
                while b != 0:
                    a, b = b, a % b
                if a == 1:
                    gcd.append(str(num2))
        if gcd:
            print(num1, '-', ", ".join(gcd))


# assert simple_task_4(2; 3; 4; 5; 6; 7)
def main():

    simple_task_4()


if __name__ == '__main__':
    main()
