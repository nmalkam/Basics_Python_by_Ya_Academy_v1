import string
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d_l = {}
d_u = {}
count = 0
# print(len(ascii_lowercase)) 26
shift = 0
query = 'Hello, world!Zz'
shift = 3
query = 'English alphabet: ABCDEFG...XYZ'
shift = -10
# shift = int(input())
shift = -1000
if shift > 0:
    start = 65 + shift
    end = 91 + shift * 2
    # как реализовать создание словаря, если я хочу чтобы при отрицательном shift словарь создавался на расстояние смещения
    # и при этом А = 65 без смещения
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
        # if count == len(ascii_lowercase):
        #     count = 0
for _ in range(start, end):
    d_u[_] = ascii_uppercase[count]  # 65-90
    d_l[_ + 32] = ascii_lowercase[count]  # 97-122
    count += 1
    if count == len(ascii_lowercase):
        count = 0
# print('shift', shift, '\n', d_u[65 + shift], 65 + shift)
# print('при 0, А 65, Н 72, E 69;  при 3, A 68')  # , ? 72;  при -10, А 65, U 72')
# print(d_u[69], 69)
# print(d_l[69 + 32], 69 + 32)
# print('new_check', d_u[ord('H') + shift * 2])
# print()
# print('check', '\n', d_u[72], 72)
# import string
# whitespace = ' \t\n\r\v\f'
# ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# import random; print(chr(random.randrange(65, 91)))
decoded = ''
for letter in query:
    if letter.isalpha():
        if letter.isupper():
            a = ord(letter)
            decoded += d_u[ord(letter) + shift * 2]
        # if not letter.isupper():
        else:
            decoded += d_l[ord(letter) + shift * 2]
        # else:
        #     decoded += chr(ord(letter) + shift)
    else:
        decoded += letter
print(query)
print(decoded)
