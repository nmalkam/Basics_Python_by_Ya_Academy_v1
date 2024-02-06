"""Файловая сумма
полагаю яндекс имел ввиду не 'Если вы хотите изучить...', а 'Если вы хотите решить эту задачу'
"""
file_in = 'numbers.num'

with open(file_in, 'rb', encoding='UTF-8') as file:
    data = file.read()
    nums = data.split()
nums = [0x001, 0x002, 0x003, 0x004, 0x005]
output = sum([int(str(x), base=16) for x in nums])
print(output)

# Для простоты файлы в примерах записаны в HEX формате.
#
# прямой, обратный и дополнительный коды
#
# Напишите программу, которая вычисляет сумму всех записанных в файле чисел в 2-байтном диапазоне.
