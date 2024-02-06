def file_weight():
    """здесь я посчитаю словарём
    ключ б:1 Б:1 КБ:1000 МБ:1000000 ГБ:1000000000"""
    import os.path
    file_name = 'file.txt'  # "file" "another_file.txt" "another_file2.txt" "another_file3.txt"
    # file_name = input()
    bit = os.path.getsize(file_name)
    file_stats = os.stat(file_name)
    # bit = file_stats.st_size
    units = {'Б': 1, 'КБ': 1000, 'МБ': 1000000, 'ГБ': 1000000000}  # 'б': 1,
    num_units = 0
    if bit > 8 :
        weight = bit / 8
    else:
        print(f'{bit}б')
        weight = bit
        # return f'{bit}б'
    while weight // (1024 ** (num_units + 1)) != 0:
        num_units += 1
    print(f'{round(weight / list(units.values())[num_units])}{list(units.keys())[num_units]}')
    # return f'{round(weight / list(units.values())[num_units])}{list(units.keys())[num_units]}'


file_weight()
