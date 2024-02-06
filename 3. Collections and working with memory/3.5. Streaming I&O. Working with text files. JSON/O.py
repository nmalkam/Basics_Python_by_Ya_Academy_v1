"""Поставь себя на моё место"""
import json
entrings = [4, 12, 3, 100, 0]
file_in = 'scoring.json'
with open(file_in, 'r+', encoding="UTF-8") as file:
    group_of_tests = json.load(file)
user_points = 0
for tests in group_of_tests:
    points = tests['points']
    points_pattern = 0
    for pattern in tests['tests']:
        # now = entrings.pop(0)
        # if str(now) == pattern['pattern']:
        if input() == pattern['pattern']:
            points_pattern += points / len(tests['tests'])
    user_points += points_pattern
print(int(user_points))
