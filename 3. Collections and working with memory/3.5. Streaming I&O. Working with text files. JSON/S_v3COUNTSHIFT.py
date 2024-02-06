def caesar_secret():
    """Это будет наш секрет
    здесь я решаю задачу путём высчитывания правильного ord в диапазоне 65 - 90 и 97 - 122
    разница с первым вариантом в том что, смещение может быть большим
    буквы неподвижны, цифры высчитываются (грубо говоря, зациклено)

    черновик взят из S_dict_v3.py"""
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shift = int(input())
    # shift = 3
    # shift = -10
    # shift = -10000
    decoded = ''
    n_sign = 1
    if shift < 0:
        n_sign = -1
    shifted_num = (abs(shift) - abs(((abs(shift) // 26) * 26))) * n_sign
    with open('public.txt', 'r', encoding='utf-8') as public:
        for num, line in enumerate(public):
            # if num == 1:
            #     shift = -10
            for letter in line:
                if letter.isalpha():
                    num_ascii = ord(letter)
                    if letter.isupper():
                        new_num = (num_ascii - 65) + shifted_num
                        if new_num >= 26:
                            new_num -= 26
                        decoded += ascii_uppercase[new_num]
                    else:
                        new_num = (num_ascii - 65 - 32) + shifted_num
                        if new_num >= 26:
                            new_num -= 26
                        decoded += ascii_lowercase[new_num]
                else:
                    decoded += letter
        with open('private.txt', 'w', encoding='utf-8') as private:
            private.write(decoded)


caesar_secret()
# Udwbyix qbfxqruj: QRSTUVW...NOP
# Khoor, zruog!
