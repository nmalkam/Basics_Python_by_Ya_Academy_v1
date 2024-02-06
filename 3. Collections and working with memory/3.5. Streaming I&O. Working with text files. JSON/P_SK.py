from sys import stdin

search_for, *file_names = [string.strip() for string in stdin]

found = False

for file_name in file_names:
    with open(file_name, encoding='UTF-8') as file:
        data = ' '.join(file.read().replace(' ', ' ').lower().split())

        if search_for.lower() in data:
            print(file_name)
            found = True

if not found:
    print('404. Not Found')
