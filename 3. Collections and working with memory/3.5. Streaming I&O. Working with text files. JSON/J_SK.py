file_name = input().strip()
lines = int(input())

with open(file_name, encoding='UTF-8') as file:
    data = [string for string in file.read().split('\n') if string]

print('\n'.join(data[-lines:]))

file_name = input()
lines = int(input())

data = []
with open(file_name) as file:
    for string in file:
        data.append(string)
for string in data[-lines:]:
    print(string.strip())
