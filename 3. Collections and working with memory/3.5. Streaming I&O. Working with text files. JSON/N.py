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
    value = users = {}
    for index in range(len(old_info)):
        name = old_info[index]["name"]
        address = old_info[index]["address"]
        phone = old_info[index]["phone"]
        if old_info[index]["address"] > update_info[index]["address"]:
            value[address] = old_info[index]["address"]
        else:
            value[address] = update_info[index]["address"]
        # if
        users[name] = value


    # for old_card in old_info:
    #     for update_card in update_info:
    #         if old_card['name'] == update_card['name']:

