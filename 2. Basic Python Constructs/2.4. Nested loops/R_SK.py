limit = int(input())

counter = 0
width = 1
max_length = 0

while counter <= limit:
    string_length = 0
    for position in range(width):
        counter += 1
        if counter <= limit:
            string_length += len(str(counter))
        if position < width - 1 and counter < limit:
            string_length += 1

    if max_length < string_length:
        max_length = string_length

    width += 1

counter = 0
width = 1

while counter <= limit:
    string = ''
    for position in range(width):
        counter += 1
        if counter <= limit:
            string += str(counter)
        if position < width - 1 and counter < limit:
            string += ' '
    width += 1
    print(f'{string:^{max_length}}')
