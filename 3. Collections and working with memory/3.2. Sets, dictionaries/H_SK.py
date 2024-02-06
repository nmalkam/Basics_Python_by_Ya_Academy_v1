porridge_eaters = dict()

for _ in range(int(input())):
    string = input()
    eater, *porridges = string.split()
    porridge_eaters[eater] = porridges

porridge = input()

names = []

for name in porridge_eaters:
    if porridge in porridge_eaters[name]:
        names.append(name)

if not names:
    print('Таких нет')
else:
    names.sort()
    for name in names:
        print(name)
