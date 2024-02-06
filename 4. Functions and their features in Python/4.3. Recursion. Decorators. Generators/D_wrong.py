# """Декор результата""" пишу код для функции без аргументов
def answer(f):
    def result(*args, **kwargs):
        return f"Результат функции: {f()}"
    return result


@answer
def a_plus_b(a, b):
    return a + b


print(a_plus_b)


@answer
def get_letters() -> str:
    return ''.join(sorted(set(filter(str.isalpha, ''))))


print(get_letters())
print(get_letters())
