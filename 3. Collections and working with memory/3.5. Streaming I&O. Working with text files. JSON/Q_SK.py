file_name = 'secret.txt'

with open(file_name, encoding='UTF-8') as file:
    data = file.read()
    decoded = ''
    for char in data:
        code = ord(char)
        code = int(code % 256) if code >= 128 else code
        decoded += chr(code)

    print(decoded)
