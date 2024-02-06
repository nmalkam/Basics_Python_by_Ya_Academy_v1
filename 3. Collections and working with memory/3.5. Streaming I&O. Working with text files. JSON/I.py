with open(input(), encoding='UTF-8') as file_one:
# with open('first.txt', encoding='UTF-8') as file_one:
    res = []
    lines = file_one.readlines()
    for line in lines:
        formated = line.strip()
        formated = formated.replace('\t', '')
        while formated.find("  ") + 1:
            formated = formated.replace("  ", " ")
        if formated:
            res.append(formated)

with open(input(), 'w', encoding='UTF-8') as answer:
# with open('second.txt', 'w', encoding='UTF-8') as answer:
    for line in res:
        answer.write(line + '\n')
