"""Слияние данных"""
import json

file_out = 'users.json'
update_file = 'updates.json'
# file_out = input().strip()
# update_file = input().strip()
with open(file_out, 'r+', encoding="UTF-8") as file:
    old_info = json.load(file)
    with open(update_file, 'r', encoding="UTF-8") as update:
        update_info = json.load(update)
    for index in range(len(old_info)):
        value = {}
        users = {}
        name = old_info[index].pop("name")
        for key in old_info[index].keys():
            pass
        # вместо этого блока я думаю что можно просто создавать словарь value,
        # а уже потом выполнять проверку на максимальное значение,
        # либо написать условие проверяю на большее если в обоих словарях найдено значение
            # try:
            #     if old_info[index][key] > update_info[index][key]:
            #         value[key] = old_info[index][key]
            #     else:
            #         value[key] = update_info[index][key]
            # except KeyError:
            #     value[key] = old_info[index][key]
        # old_info[index]['name'] = name
        for k in update_info[index].keys():
            if k not in old_info[index].keys():
                value[k] = update_info[index][k]
        users[name] = value
