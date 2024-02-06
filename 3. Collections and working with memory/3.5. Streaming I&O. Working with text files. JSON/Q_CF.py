# CF = CyberForum.ru
str1 = '᥈୥ᙬᱬᝯ, ᭷ᝯ୲੬๤!'
print(''.join(chr(ord(i) & 255) for i in str1))

s = '᥈୥ᙬᱬᝯ, ᭷ᝯ୲੬๤!'
res = ''.join(map(lambda i: chr(ord(i) % 128), s))
print(res)
