def my_func(num_a, num_b, num_c):
    def dic(num):
        num = str(num)
        num_map = {}
        n = len(str(num))
        for item in range(n):
            num_map[num[item]] = item + 1
        # print(num_map)
        return num_map

    def all_in_one(dictionaries):
        index = 0
        dic_map = {}
        for item in range(len(dictionaries)):
            dic_map[item] = dictionaries[item]
            index += 1
        # print(dic_map)
        return dic_map

    def check_complement(dictionary):
        print(dictionary.keys())
        print(type(dictionary))
        result = []
        count_k = 0
        for k, val in dictionary.items():
            print(dictionary.keys())
            if k == dictionary.keys():
                count_k += 1
                result.append(k)
                if count_k == len(dictionary):
                    print("Found")
                    return k
            elif isinstance(val, dict):
                nested_result = check_complement(val)
                result.extend(nested_result)
        return result

    # result = []
    dic_num_a = dic(num_a)
    dic_num_b = dic(num_b)
    dic_num_c = dic(num_c)
    list_dic = [dic_num_a, dic_num_b, dic_num_c]
    # all_in_one(list_dic)
    # print(all_in_one(list_dic))
    # all_in_one_me = {1: dic_num_a, 2.2.Conditional operator: dic_num_b, 3: dic_num_c}
    # print(all_in_one_me)
    # check_complement(all_in_one_me)
    check_complement(all_in_one(list_dic))


assert my_func(12, 13, 14) == 1
assert my_func(12, 41, 14) == []
assert my_func(23, 13, 63) == 3
print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    num_a = input()
    num_b = input()
    num_c = input()
    print(my_func(num_a, num_b, num_c))


if __name__ == '__main__':
    main()
