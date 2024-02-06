import json

file_in = input().strip()
file_out = input().strip()

with open(file_in, encoding="UTF-8") as file:
    numbers = [int(number) for number in file.read().split()]

stat = {
    "count": (length := len(numbers)),
    "positive_count": len([number for number in numbers if number > 0]),
    "min": min(numbers),
    "max": max(numbers),
    "sum": (total := sum(numbers)),
    "average": float(f"{(total / length):.2f}"),
}

with open(file_out, "w", encoding="UTF-8") as file:
    json.dump(stat, file, ensure_ascii=False, indent=4)
