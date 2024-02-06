"""каретка, указатель"""
file_in = 'first.txt'
n = 2
# file_in = input()
# n = input()
rows = 0
with open(file_in, 'r', encoding="UTF-8") as file_in:
    line_count = sum(1 for line in file_in)
    file_in.seek(0)
    for line in file_in.readlines():
        rows += 1
        if rows > line_count - n:
            print(line, end='')
