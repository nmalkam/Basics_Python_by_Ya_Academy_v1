with open(input(), encoding='UTF-8') as file_one:
    # with open('first.txt', encoding='UTF-8') as file_one:
    res = []
    lines = file_one.readlines()
    for line in lines:
        strng = line.strip()
        lst = list(strng)
        stack = []
        semi_res = ''
        while lst:
            current = lst.pop(0)
            if len(stack) == 0:
                stack.append(current)
            elif stack[-1] == current == ' ':
                continue
            elif stack[-1] == current == '\n':
                continue
            elif current == '\t':
                continue
            else:
                stack.append(current)
        semi_res = ''.join(stack)
        if not semi_res:
            continue
        res.append(semi_res)
with open(input(), 'w', encoding='UTF-8') as answer:
    # with open('second.txt', 'w', encoding='UTF-8') as answer:
    for line in res:
        answer.write(line + '\n')
