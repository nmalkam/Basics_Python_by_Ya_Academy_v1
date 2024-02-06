def a():
    # text = 'Мама мыла раму!'
    # text = '''Ехали медведи
    # На велосипеде.
    #
    # А за ними кот
    # Задом наперёд.'''

    # print((num for num in numbers if num % (num ** 0.5) == 0))
    # print(set([num for num in numbers if num % (num ** 0.5) == 0]))

    # [char: char.get(char, 0) + 1 for char in word]
    text = list(text.lower().replace('.', '').replace('!', '').replace(' ', '').replace('\n', ''))
    chars = [char for char in sorted(set(text))]
    # print(chars)
    counts = [text.count(char) for char in sorted(set(text))]
    # print(counts)
    lst_ch_co = []
    for _ in range(len(chars)):
        x = [chars[_]]
        x.append(counts[_])
        lst_ch_co.append(x)
    # print(lst_ch_co)
    d = {char: count for char, count in lst_ch_co}
    print(d)
    return d
a()
# [("Беларусь", "Минск"),
# text.count(char) for char in text

# cities = ['Austin', 'Tacoma', 'Topeka', 'Sacramento', 'Charlotte']
# temps = {city: [0 for _ in range(7)] for city in cities}


    # [char: char.get(char, 0) + 1 for char in word]
# for word in text.replace('.', '').split())}
# print(set([char for char in word] for word in text.replace('.', '').split()))

# countries = {country: capital for country, capital in
#              [("Беларусь", "Минск"),
#               ("Сербия", "Белград")]}
# print(countries)

# text = 'Мама мыла раму!'
# {'а': 4, 'л': 1, 'м': 4, 'р': 1, 'у': 1, 'ы': 1}
