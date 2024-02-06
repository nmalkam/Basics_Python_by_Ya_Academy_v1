"""Прятки"""
with open('secret.txt', 'r', encoding='utf-8') as file:
    text = [line.strip() for line in file.readline()]
for char in text:
    if char:
        small_byte = ord(char) % 128
        print(chr(small_byte), end='')
    # print(chr(ord(char)) & 255)





# ᥈୥ᙬᱬᝯ, ᭷ᝯ୲੬๤!
# мы используем порядок от старшего к младшему(big-endian — с большого конца: An-1,...A0)
# {по причине порядка записи информации в память}
# поэтому при получении результата от функции ord(char)
# мы должны убрать лишнее(поделить на 256
# {по причине того что данные записываются длинной 128 ##### но с разным знаком,
# то есть 128 * 2})
#
