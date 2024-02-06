# Вы можете модифицировать рекурсивную функцию search_value_in_dict для поиска всех значений,
# где ключ равен 1. Вот пример кода:
def search_key_in_dict(key, dictionary):
    result = []
    for k, val in dictionary.items():
        if k == key:
            result.append(val)
        elif isinstance(val, dict):
            nested_result = search_key_in_dict(key, val)
            result.extend(nested_result)
    return result
# Пример использования:
all_dict = {"dict_1": {1:1, 2:2}, "dict_2": {1:1, 3:2}, "dict_3": {1:1, 4:2}, "dict_4": {1:1, "dict_5":{1:1, 56:2}}}
result = search_key_in_dict(1, all_dict)
# }  #
print(result)  # Выводит: [1, 1, 1]
# В этом примере функция search_key_in_dict рекурсивно проходит по всем элементам словаря
# и его вложенных словарей, ищет заданный ключ и возвращает список значений, где этот ключ был найден.
