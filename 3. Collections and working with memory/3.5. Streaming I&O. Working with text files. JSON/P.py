"""Найдётся всё 3.0"""
from sys import stdin
# query = 'a b'.lower()
# query = 'Мама мыла РАМУ'.lower()
# file_names = ['firstP.txt', 'secondP.txt']
file_names = []
query = input().strip().lower()
for line in stdin:
    file_names.append(line.strip())
res = 0
for name in file_names:
    with open(name, 'r', encoding="UTF-8") as file:
        strng_content = ''
        for line in file:
            if line.strip():
                strng_content += line.lower().strip() + ' '
        while strng_content.find('\t') + 1:
            strng_content.replace('\t', ' ')
        while strng_content.find('&nbsp;') + 1:
            strng_content = strng_content.replace('&nbsp;', ' ')
        while strng_content.find('\\n') + 1:
            strng_content = strng_content.replace('\\n', ' ')
        while strng_content.find('  ') + 1:
            strng_content = strng_content.replace('  ', ' ')
        if query in strng_content:
            print(name)
            res += 1
if res == 0:
    print("404. Not Found")

# 'a\\nb'
