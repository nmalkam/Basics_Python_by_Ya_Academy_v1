# """Декор результата"""
def answer(f):
    def result(*args, **kwargs):
        return f"Результат функции: {f(*args, **kwargs)}"
    return result


@answer
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5))


@answer
def get_letters(text: str) -> str:
    return ''.join(sorted(set(filter(str.isalpha, text.lower()))))


print(get_letters('Hello, world!'))
print(get_letters('Декораторы это круто =)'))
