# sequence_1 = 'Иванов'
# sequence_2 = 'qванов'
# # elif all(item not in r'[а-яА-ЯёЁ]' for item in last_name_first_name):
# #     print(7)
# for item in sequence_2:
#     if item in r'[а-яА-ЯёЁ]':
#         print(123)

# if all(item in r'[а-яА-ЯёЁ]' for item in 'qванов'):
#     print(13)
print(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$')
word = 'Иванов'
word = 'qванов'

print([item.lower() not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' for item in word])
for _ in word:
    if _.lower() not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
        print(123)
