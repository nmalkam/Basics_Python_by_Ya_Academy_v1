def caesar_secret():
    """Это будет наш секрет"""
    # shift = int(input())
    shift = 3
    # shift = -10
    decoded = ''
    with open('public.txt', 'r', encoding='utf-8') as public:
        for line in public:
            for num, letter in enumerate(line):
                if num == 2:
                    shift = -10
                if letter.isalpha():
                    # сперва реши на бумаге
                    #
                    #
                    # .
                    # if ord(letter) < 65 or 90 < ord(letter) < 97:
                    decoded += chr(ord(letter) + shift)
                else:
                    decoded += letter
        with open('private.txt', 'w', encoding='utf-8') as private:
            private.write(decoded)


caesar_secret()
# Udwbyix qbfxqruj: QRSTUVW...NOP
# Khoor, zruog!


for num, letter in enumerate(line):
    if num == 2:
        shift = -10
