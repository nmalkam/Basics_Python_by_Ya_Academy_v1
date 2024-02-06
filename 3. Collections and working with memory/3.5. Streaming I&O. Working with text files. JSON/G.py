def file_statistics():
    file_name = input()
    with open(file_name, 'r', encoding='UTF-8') as entring:
        lines = entring.readlines()
    # with open('G_file_statistics.txt', 'w', encoding='utf-8') as outputed:
    n = 0
    positive = 0
    min = 10000
    max = -10000
    summ = 0
    average = 0
    for line in lines:
        lst_nums = line.rstrip('\n').split()
        # print(len(lst_nums))
        # print(sum([int(positive) for positive in lst_nums if int(positive) > 0]))
        for num in lst_nums:
            num = int(num)
            n += 1
            if num > 0:
                positive += 1
            if num < min:
                min = num
            if num > max:
                max = num
            summ += num
    average = round(summ / n, 2)
    print(str(n))
    print(str(positive))
    print(str(min))
    print(str(max))
    print(str(summ))
    print(str(average))


file_statistics()
