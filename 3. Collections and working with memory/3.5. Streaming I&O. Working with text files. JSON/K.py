import json

# file_in = input().strip()
# file_out = input()
file_in = 'numbers.txt'
file_out = 'statistics.json'

with open(file_in, encoding='UTF-8') as file_in:
    numbers = [int(number) for number in file_in.read().split() if number]
stats = {
    'count': (length := len(numbers)),
    'positive_count': len([num for num in numbers if num > 0]),
    'min': min(numbers),
    'max': max(numbers),
    'sum': (total := sum(numbers)),
    'average': float(f'{(total / length):.2f}')
}
with open(file_out, 'w', encoding='UTF-8') as file_out:
    json.dump(stats, file_out, ensure_ascii=False, indent=4)
