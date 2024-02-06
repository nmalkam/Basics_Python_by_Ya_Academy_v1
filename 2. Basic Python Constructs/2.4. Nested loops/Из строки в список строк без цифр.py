# Меньше250Меньше125Больше188Меньше156Больше172Меньше164Больше168Больше170Больше171Угадал!
'''3
березка
елочка
зайка
волк
березка
ВСЁ
сосна
сосна
сосна
елочка
грибочки
медведь
ВСЁ
сосна
сосна
сосна
белочка
сосна
белочка
ВСЁ'''
string = '''зайка
березка
ВСЁ
зайка
зайка
ВСЁ
березка
елочка
березка
ВСЁ
елочка
елочка
елочка
ВСЁ'''
# result = []
for i in string:
    result = string.split('\n')
print(result)




# for item in string:
#     if item.isdigit():
#         string.replace(item, " ")
# НЕ РАБОТАЕТ                                                       пОЧЕМУ?????

# res = "".join(filter(lambda x: not x.isdigit(), string))
#
# res = ''.join([i for i in string if not i.isdigit()])
# rewrewrwerewr
print()
# num = "1234567890"
# str2 = ""
# for i in string:
#     if i in num:
#         str2 += i
#     else:
#         str2 += ' '
#
# listed = sorted(str2.split(' '))  # [-9:]
# inte = []
# for integer in listed:
#     inte.append(int(integer))  # удалили чтото по типу [-9:]
#
# print(inte[::-1])
#
# print(listed)
