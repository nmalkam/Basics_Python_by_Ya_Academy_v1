text = 'Мама мыла раму!'
# text = '''Ехали медведи
# На велосипеде.
#
# А за ними кот
# Задом наперёд.'''

# result = {}
#
for letter in set(text.lower()):
    if letter.isalpha():
        result[letter] = text.lower().count(letter)

d = {char: text.lower().count(char) for char in set(text.lower()) if char.isalpha()}

# d = {char: text.count(char) for char in set(text.lower()) if char.isalpha()}

d = {char: text.lower().count(char) for char in set(text.lower()) if char.isalpha()}
print(d)
