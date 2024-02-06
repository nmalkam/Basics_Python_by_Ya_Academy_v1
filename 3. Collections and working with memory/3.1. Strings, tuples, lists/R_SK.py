string = input()

current_char = string[0]
current_length = 1

for char in string[1:]:
    if current_char == char:
        current_length += 1
    else:
        print(current_char, current_length)
        current_char = char
        current_length = 1

print(current_char, current_length)
