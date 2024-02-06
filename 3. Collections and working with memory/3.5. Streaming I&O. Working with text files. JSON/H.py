# file_difference
with open(input(), encoding='UTF-8') as file_one:
    words_1 = set([word for word in file_one.read().split()])
with open(input(), encoding='UTF-8') as file_two:
    words_2 = set([word for word in file_two.read().split()])
words_3 = words_1.symmetric_difference(words_2)
with open(input(), 'w', encoding='UTF-8') as answer:
    for word in sorted(set(words_3)):
        answer.write(word + '\n')

# first.txt
# second.txt
# answer.txt
