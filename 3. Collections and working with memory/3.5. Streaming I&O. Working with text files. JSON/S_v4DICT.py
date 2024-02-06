def caesar_secret():
    """Это будет наш секрет
    здесь я решаю задачу путём создания двух словарей по подсказке из теории SK

    черновик взят из S_dict_v3.py"""
    ascii = 'abcdefghijklmnopqrstuvwxyz'
    LETTERS = {}  # keys is original alphabet and values shifted alphabet
    shift = int(input())
    shifted_num = abs(shift) - abs(((abs(shift) // 26) * 26))
    if shift < 0:
        shifted_num *= -1
    shifted_ascii = ascii[shifted_num:] + ascii[:shifted_num]
    # shift = 3
    # shift = -10
    # shift = -10000
    decoded = ''
    for _ in range(26):
        LETTERS[ascii[_]] = shifted_ascii[_]
    with open('public.txt', 'r', encoding='utf-8') as public:
        for num, line in enumerate(public):
            for letter in line:
                if letter.isalpha():
                    if letter.isupper():
                        decoded += LETTERS[letter.lower()].upper()
                    else:
                        decoded += LETTERS[letter].lower()
                else:
                    decoded += letter
        with open('private.txt', 'w', encoding='utf-8') as private:
            private.write(decoded)


caesar_secret()
# Udwbyix qbfxqruj: QRSTUVW...NOP
# Khoor, zruog!
