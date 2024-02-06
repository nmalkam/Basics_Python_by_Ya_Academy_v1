sum = 0
while True:
    price = float(input("Введите число (для завершения введите 0): "))
    if price == 0:
        break
    elif price >= 500:
        price = price * 0.9
    sum += price
print(sum)
