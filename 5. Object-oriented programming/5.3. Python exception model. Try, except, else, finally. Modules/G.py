class NameValidation(Exception):
    pass


class CyrillicError(NameValidation):
    pass


class CapitalError(NameValidation):
    pass


def name_validation(last_name_or_first_name):
    if not isinstance(last_name_or_first_name, str):
        raise TypeError
    elif any([item.lower() not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' for item in last_name_or_first_name]):
        raise CyrillicError
    elif last_name_or_first_name != last_name_or_first_name.capitalize():
        raise CapitalError
    else:
        return last_name_or_first_name


# r'[а-яА-ЯёЁ]'
# 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
print(name_validation("Иванов"))
# print(name_validation("Иqванов"))
# print(name_validation("user"))
# Вызвано исключение CyrillicError
# print(name_validation("иВанов"))
# print(name_validation("1иванов"))
# print(name_validation("ИВАНОВ"))
# Вызвано исключение CapitalError
