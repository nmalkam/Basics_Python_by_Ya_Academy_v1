# string = 'Российская Федерация'
string = 'открытое акционерное общество'
# 'РФ'
# 'ОАО'

''.join([char for char in string.upper() if char.isalpha()])
# print(''.join([char for char in string.upper() if char.isalpha()]))

res = ''
for word in string.split():
    # res += ''.join([word[0].upper()])
    res += word[0].upper()
print(res)

''.join([word[0].upper() for word in string.split()])
# print(''.join([word[0].upper() for word in string.split()]))
