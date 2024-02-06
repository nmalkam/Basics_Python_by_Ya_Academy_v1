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
    users = {}
    for index in range(len(old_info)):
        value = {}
        name = old_info[index].pop("name")
        for key in old_info[index].keys():
            if key in update_info[index].keys():
                if old_info[index][key] > update_info[index][key]:
                    value[key] = old_info[index][key]
                else:
                    value[key] = update_info[index][key]
            else:
                value[key] = old_info[index][key]
        old_info[index]['name'] = name
        for k in update_info[index].keys():
            if k not in old_info[index].keys():
                value[k] = update_info[index][k]
        users[name] = value

    file.seek(0)
    json.dump(users, file, ensure_ascii=False, indent=4)
