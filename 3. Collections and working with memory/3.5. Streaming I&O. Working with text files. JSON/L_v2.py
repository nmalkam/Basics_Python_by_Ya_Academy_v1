"""создаю файл целиком
divide_and_rule"""
file_in = input().strip()
evens_file = input().strip()
odds_file = input().strip()
equals_file = input().strip()
# file_in = 'numbers_DAR.txt'
# even_file = 'even.txt'
# odd_file = 'odd.txt'
# eq_file = 'eq.txt'

with open(file_in, encoding="UTF-8") as file:
    enter = '\n'
    even_nums, odd_nums, eq_nums = '', '', ''
    for line in file.readlines():
        for number in line.split():
            count_even = len([num for num in number if int(num) % 2 == 0])
            if count_even > len(number) / 2:
                even_nums += f'{number} '
            elif count_even < len(number) / 2:
                odd_nums += f'{number} '
            else:
                eq_nums += f'{number} '
        even_nums += enter
        odd_nums += enter
        eq_nums += enter

with open(evens_file, 'w', encoding="UTF-8") as even:
    even.write(even_nums)
with open(odds_file, 'w', encoding="UTF-8") as odd:
    odd.write(odd_nums)
with open(equals_file, 'w', encoding="UTF-8") as eq:
    eq.write(eq_nums)
