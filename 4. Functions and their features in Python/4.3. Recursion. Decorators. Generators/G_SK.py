# def same_type(func):
#     def wrapper(*args):
#         type_of_first = type(args[0])
#         if all(type(item) == type_of_first for item in args[1:]):
#             return func(*args)
#         else:
#             print('Обнаружены различные типы данных')
#     return wrapper


def same_type(func):
    def wrapper(*args):
        # res = {}
        # for item in args:
        #
        if len({type(item) for item in args}) != 1:
            print("Обнаружены различные типы данных")
            return False
        return func(*args)
    return wrapper


@same_type
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5.2) or 'Fail')
print(a_plus_b(7, '9') or 'Fail')
print(a_plus_b(-3, 5) or 'Fail')
