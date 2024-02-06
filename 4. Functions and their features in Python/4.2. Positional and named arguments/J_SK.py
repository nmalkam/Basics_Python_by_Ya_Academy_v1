def secret_replace(text, **code):
    new_text = ''
    code = {key: [value, 0] for key, value in code.items()}
    for char in text:
        if char in code:
            pos = code[char][1] % len(code[char][0])
            new_text += code[char][0][pos]
            code[char] = [0], [pos + 1]
        else:
            new_text += char
    return new_text

def secret_replace(text, **code):
    new_text = ''
    for char in text:
        if char in code:
            new_text += code[char][0]
            code[char] = code[char][1:] + (code[char][0],)
        else:
            new_text += char
    return new_text


# Пример кода с ошибкой, который проходит тесты.

def secret_replace(text, **code):
    for item in code:
        while item in text:
            for substitution in code[item]:
                if item in text:
                    text = text[:text.find(item)] + substitution + text[text.find(item) + 1:]
    return text
