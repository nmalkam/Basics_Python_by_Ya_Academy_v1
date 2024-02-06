def same_type(f):
    def wrapper(*args):
        for _ in args[1:]:
            # if type(args[0]) != type(_):
            if type(args[0]) is not type(_):
                print("Обнаружены различные типы данных")
                return 0
        else:
            return f(*args)
    return wrapper


@same_type
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5.2) or 'Fail')
print(a_plus_b(7, '9') or 'Fail')
print(a_plus_b(-3, 5) or 'Fail')


@same_type
def combine_text(*words):
    return ' '.join(words)


# print(combine_text('Hello,', 'world!') or 'Fail')
# print(combine_text(2, '+', 2, '=', 4) or 'Fail')
# print(combine_text('Список из 30', 0, 'можно получить так', [0] * 30) or 'Fail')
