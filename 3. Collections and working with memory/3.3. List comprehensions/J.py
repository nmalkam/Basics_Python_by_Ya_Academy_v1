rle = [('a', 2, 4), ('b', 3, 1), ('c', 1, 2)]
# rle = [('1', 1), ('0', 2), ('5', 1), ('0', 2)]
# 'aabbbc'
# '100500'



# print(' - '.join(map(str, sorted(set(numbers)))))
res = ''
for elem in rle:
    res += elem[0] * elem[1]
    # print([elem[0] * elem[1]])
# print(res)

# ''.join([elem[0] * elem[1] for elem in rle])
# print(''.join([elem[0] * elem[1] for elem in rle]))


# от SK

print(''.join(char * count + str(c) for char, count, c in rle))

# result = ''
# chars = []
#
# for char, count in rle:
#     chars.append(char * count)
#
# result = ''.join(chars)
