"""Обновление данных"""
import json
from sys import stdin

# file_out = 'data.json'
# lines = ['one == один',
#          'two == два',
#          'three == три']
file_out = input().strip()
d_entrings = {}
# for line in lines:
for line in stdin:
    key, value = line.strip().split(' == ')
    d_entrings[key] = value

with open(file_out, 'r+', encoding="UTF-8") as file:
    obj = json.load(file)
    for key, value in d_entrings.items():
        obj[key] = value
    file.seek(0)
    json.dump(obj, file, ensure_ascii=False, indent=4)
