def frequency_analysis_at_minimum_prices():

    first_alpha_list = []
    alpha_dict = {}

    while (string := input()) != 'ФИНИШ':
        string = string.lower().replace(' ', '')
        for letter in string:
            if letter not in alpha_dict.keys():
                alpha_dict[letter] = 1
            elif letter in alpha_dict.keys():
                alpha_dict[letter] += 1
        # полагаю можно попробовать выводить все ключи с максимальным значением словаря
        # и уже(например) их отсортировать и выводить первый по алфавиту
        # можно сделать дополнительно проверку, чтобы не прогонять каждый раз словарь
        # если в нём максимальное значение только одно
    for k in alpha_dict:
        if alpha_dict[k] == max(alpha_dict.values()):
            first_alpha_list.append(k)
    # first_alpha_list.append([k for k in alpha_dict if alpha_dict[k] == max(alpha_dict.values())])
    res = sorted(first_alpha_list)
    print(res[0])


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    frequency_analysis_at_minimum_prices()


if __name__ == '__main__':
    main()
