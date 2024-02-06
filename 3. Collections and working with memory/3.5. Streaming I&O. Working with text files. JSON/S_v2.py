def caesar_secret():
    """Это будет наш секрет
    здесь я решаю задачу путём копирования букв в новый цикл
    грубо говоря в первом случае мы двигаем цифры, буквы стоят на месте,
    в этом варианте делаем наоборот
    цифры неподвижны, буквы копируются зациклено

    черновик взят из S_dict_v2.py"""
    # shift = int(input())
    shift = 3
    # shift = 10
    # shift = -1000
    decoded = ''
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d_l = {}
    d_u = {}
    count = 0
    with open('public.txt', 'r', encoding='utf-8') as public:
        if shift > 0:
            start = 65 + shift
            end = 91 + shift * 2
        else:
            start = 65 + shift
            end = 91 + shift
            counter = 65 + shift * 2
            pos = shift
            while counter != start:
                d_u[counter] = ascii_uppercase[pos]  # 65-90
                d_l[counter + 32] = ascii_lowercase[pos]  # 97-122
                counter += 1
                pos += 1
        for _ in range(start, end):
            d_u[_] = ascii_uppercase[count]  # 65-90
            d_l[_ + 32] = ascii_lowercase[count]  # 97-122
            count += 1
            if count == len(ascii_lowercase):
                count = 0
        for line in public:
            for letter in line:
                if letter.isalpha():
                    if letter.isupper():
                        decoded += d_u[ord(letter) + shift * 2]
                    else:
                        decoded += d_l[ord(letter) + shift * 2]
                else:
                    decoded += letter
        with open('private.txt', 'w', encoding='utf-8') as private:
            private.write(decoded)


caesar_secret()
# Udwbyix qbfxqruj: QRSTUVW...NOP
# Khoor, zruog!
