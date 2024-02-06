"""Слияние данных
Только что переписал свое старое решение на такое:
читаем первый файл, создаем из него словарь требуемого вида.
читаем второй файл, перебираем словари из него.
для каждого ключа в словаре, кроме имени конечно, сравниваем
 (при наличии, если такого нет, то подразумеваем пустую строку) старое значение и новое,
  если старое меньше чем новое, то обновляем.
записываем словарь в файл"""
import json

file_out = 'users.json'
update_file = 'updates.json'
# file_out = input().strip()
# update_file = input().strip()
with open(file_out, 'r+', encoding="UTF-8") as file:
    users = {}
    old_info = json.load(file)
    for index in range(len(old_info)):
        name = old_info[index]['name']
        value = {}
        users[name] = value
        for key in old_info[index].keys():
            if key != 'name':
                value[key] = old_info[index][key]
    with open(update_file, 'r', encoding="UTF-8") as update:
        update_info = json.load(update)
        for dict in update_info:
            name = dict['name']
            for k in dict.keys():
                if k != 'name':
                    if users[name].get(k, '') < dict[k]:
                        users[name][k] = dict[k]

    file.seek(0)
    json.dump(users, file, ensure_ascii=False, indent=4)
