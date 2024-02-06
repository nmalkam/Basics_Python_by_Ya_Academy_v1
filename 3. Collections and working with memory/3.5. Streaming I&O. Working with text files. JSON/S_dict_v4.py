ascii = 'abcdefghijklmnopqrstuvwxyz'
LETTERS = {}  # keys is original alphabet and values shifted alphabet
# print(len(ascii_lowercase))  # 26
shift = 0
query = 'ZHello, world!Zz'
shift = 3
query = 'XYZEnglish alphabet: ABCDEFG...XYZ'
shift = -10
# shift = -1000
decoded = ''
shifted_num = abs(shift)-abs(((abs(shift)//26)*26))
if shift < 0:
    shifted_num *= -1
shifted_ascii = ascii[shifted_num:] + ascii[:shifted_num]
for _ in range(26):
    LETTERS[ascii[_]] = shifted_ascii[_]
for letter in query:
    if letter.isalpha():
        if letter.isupper():
            decoded += LETTERS[letter.lower()].upper()
        else:
            decoded += LETTERS[letter].lower()

    else:
        decoded += letter

print(query)
print(decoded)
# Udwbyix qbfxqruj: QRSTUVW...NOP
# Khoor, zruog!
