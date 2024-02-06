# input_file = input()
# evens_file = input()
# odds_file = input()
# equals_file = input()
file_in = 'numbers_DAR.txt'
even_file = 'even.txt'
odd_file = 'odd.txt'
eq_file = 'eq.txt'


with open(file_in, encoding="UTF-8") as file:
    strings = [string for string in file.read().split("\n") if string]

even_digits = "02468"
odd_digits = "13579"

for string in strings:
    evens, odds, equals = [], [], []

    for number in string.split():
        total_evens = total_odds = 0
        for char in number:
            if char in even_digits:
                total_evens += 1
            elif char in odd_digits:
                total_odds += 1

        if total_evens > total_odds:
            evens.append(number)
        elif total_evens < total_odds:
            odds.append(number)
        else:
            equals.append(number)

    with open(even_file, "a", encoding="UTF-8") as file:
        file.write(" ".join(evens) + "\n")
    with open(odd_file, "a", encoding="UTF-8") as file:
        file.write(" ".join(odds) + "\n")
    with open(eq_file, "a", encoding="UTF-8") as file:
        file.write(" ".join(equals) + "\n")
