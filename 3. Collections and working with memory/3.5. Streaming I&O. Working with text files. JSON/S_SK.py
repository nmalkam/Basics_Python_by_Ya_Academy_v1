# file_in = 'public.txt'
# file_out = 'private.txt'
#
# a = ord('a')
# z = ord('z')
#
# shift = int(input()) % 26
#
# with open(file_in, encoding='UTF-8') as file:
#     data = file.read()
#
#     output = ''
#
#     for i in range(len(data)):
#         print(len(data))
#         pos = a
#         if a <= (code := ord(data[i].lower())) <= z:
#             pos = code + shift
#             if pos > z:
#                 pos -= 26
#             elif pos < a:
#                 pos += 26
#             output += chr(pos).upper() if data[i].isupper() else chr(pos)
#         else:
#             output += data[i]
#
# print(output)
# # with open(file_out, 'w', encoding='UTF-8') as file:
# #     file.write(output)
'''
'''
# file_in = 'public.txt'
# file_out = 'private.txt'
#
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
#
# shift = int(input()) % len(alphabet)
#
# shifted_alphabet = alphabet[shift:] + alphabet[:shift]
# output = ''
#
# with open(file_in, encoding='UTF-8') as file:
#     data = file.read()
#
#     for char in data:
#         new_char = char
#         if char.lower() in alphabet:
#             pos = alphabet.find(char.lower())
#             new_char = shifted_alphabet[pos]
#         output += new_char.upper() if char.isupper() else new_char
#
# # print(output)
# with open(file_out, 'w', encoding='UTF-8') as file:
#     file.write(output)
'''
'''
file_in = 'public.txt'
file_out = 'private.txt'

chars = 'abcdefghijklmnopqrstuvwxyz'

shift = int(input()) % len(chars)

shifted_chars = chars[shift:] + chars[:shift]

alphabet = {key: value for key, value in zip(chars, shifted_chars)}
output = ''

with open(file_in, encoding='UTF-8') as file:
    data = file.read()

    for char in data:
        new_char = alphabet[char.lower()] if char.lower() in alphabet else char
        output += new_char.upper() if char.isupper() else new_char

# print(output)
# with open(file_out, 'w', encoding='UTF-8') as file:
#     file.write(output)
