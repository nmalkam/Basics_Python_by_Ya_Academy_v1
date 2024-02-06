subject = 'зайка'
objects = []

while (nature := input().split()) != '':
    if len(nature) > 1 and subject in nature:
        for pos in range(length := len(nature)):
            if nature[pos] == subject:
                if pos == 0:
                    objects.append(nature[1])
                elif pos == (length - 1):
                    objects.append(nature[-2])
                else:
                    objects.append(nature[pos - 1])
                    objects.append(nature[pos + 1])

for object in set(objects):
    print(object)
