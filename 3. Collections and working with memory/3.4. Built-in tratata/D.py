from itertools import accumulate

for value in accumulate([item + ' ' for item in input().split()]):
    print(value)
