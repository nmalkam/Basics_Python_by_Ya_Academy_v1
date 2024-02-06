count = 0
raws = 25  # int(input())
res = []

while count != raws + 1:
    # if count == raws:
    # print('')
    # print(f'{input()}')
    # else:
    if (inputed := input()).isdigit():
        print(f"{inputed}, ")
    else:
        print(f"'{inputed}', ")
    count += 1


#     res.append(str(input()))
#     count += 1
# for item in res:
#     print(item)



#
# for i in string:
#     if i in num:
#         str2 += i
#     else:
#         str2 += ' '
#
# listed = sorted(str2.split(' '))[-9:]
# inte = []
# for integer in listed:
#     inte.append(int(integer))
#
# print(inte[::-1])
#
# print(listed)

# TRANSLITERATION
# while count != raws + 1:
#     str = input().replace(' ', '').replace('—', ': ')
#     print(f"'{str}', ")
#
#     count += 1
