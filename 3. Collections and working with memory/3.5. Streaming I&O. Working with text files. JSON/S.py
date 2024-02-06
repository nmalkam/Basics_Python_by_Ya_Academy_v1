def caesar_secret():
    """Это будет наш секрет
    здесь я решаю задачу путём высчитывания правильного ord в диапазоне 65 - 90 и 97 - 122
    буквы неподвижны, цифры высчитываются (грубо говоря, зациклено)"""
    # shift = int(input())
    # shift = 3
    shift = -10
    shift = -1000
    decoded = ''
    with open('public.txt', 'r', encoding='utf-8') as public:
        for num, line in enumerate(public):
            # if num == 1:
            #     shift = -10
            for letter in line:
                if letter.isalpha():
                    if letter.isupper():
                        if ord(letter) + shift < 65:
                            recounted_letter = 91 + (shift + (ord(letter) - 65))
                            decoded += chr(recounted_letter)
                            continue
                        elif ord(letter) + shift > 90:
                            recounted_letter = 64 + (shift + (ord(letter) - 90))
                            decoded += chr(recounted_letter)
                            continue
                        else:
                            decoded += chr(ord(letter) + shift)
                            continue
                    if not letter.isupper():
                        if ord(letter) + shift < 97:
                            recounted_letter = 123 + (shift + (ord(letter) - 97))
                            decoded += chr(recounted_letter)
                            continue
                        elif ord(letter) + shift > 122:
                            recounted_letter = 96 + (shift + (ord(letter) - 122))
                            decoded += chr(recounted_letter)
                            continue
                        else:
                            decoded += chr(ord(letter) + shift)
                            continue
                    else:
                        decoded += chr(ord(letter) + shift)
                else:
                    decoded += letter
        with open('private.txt', 'w', encoding='utf-8') as private:
            private.write(decoded)


caesar_secret()
# Udwbyix qbfxqruj: QRSTUVW...NOP
# Khoor, zruog!
