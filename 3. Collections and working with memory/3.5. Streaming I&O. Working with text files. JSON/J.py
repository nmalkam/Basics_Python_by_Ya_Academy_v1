file_in = 'first.txt'
n = 2
# file_in = input()
# n = int(input())

lines = []
with open(file_in, 'r', encoding="UTF-8") as file_in:
    for line in file_in.readlines():
        lines.append(line.strip())
lines = lines[len(lines) - n:]
for _ in range(n):
    print(lines[_])
