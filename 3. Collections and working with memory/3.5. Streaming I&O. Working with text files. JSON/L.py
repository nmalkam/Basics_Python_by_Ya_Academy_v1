"""создаю файл построчно
divide_and_rule"""
file_in = input().strip()
even_file = input().strip()
odd_file = input().strip()
eq_file = input().strip()
# file_in = 'numbers.txt'
# even_file = 'even.txt'
# odd_file = 'odd.txt'
# eq_file = 'eq.txt'

with open(file_in, encoding="UTF-8") as file:
    for line in file.readlines():
        even_nums, odd_nums, eq_nums = [], [], []
        for number in line.split():
            count_even = len([num for num in number if int(num) % 2 == 0])
            if count_even > len(number) / 2:
                even_nums.append(number)
            elif count_even < len(number) / 2:
                odd_nums.append(number)
            else:
                eq_nums.append(number)

        with open(even_file, 'a', encoding="UTF-8") as even:
            even.write(' '.join(even_nums) + '\n')
        with open(odd_file, 'a', encoding="UTF-8") as odd:
            odd.write(' '.join(odd_nums) + '\n')
        with open(eq_file, 'a', encoding="UTF-8") as eq:
            eq.write(' '.join(eq_nums) + '\n')
