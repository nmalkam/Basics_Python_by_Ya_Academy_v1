def simple_task_4():  # 2.4. Вложенные циклы K.Простая задача_3 Simple task 3

    def mutually_prime(key_num: int, val_num: int) -> bool:
        for i in range(2, max(key_num, val_num)+1):
            if key_num % i == 0:
                if val_num % i == 0:
                    return False
        return True

    d_nums = {}

    nums = list(map(int, input().split('; ')))

    for key in nums:
        for val in nums:
            if mutually_prime(key, val):
                d_nums[key] = d_nums.get(key, '') + f'{val}, '

        # for i in range(2, max(key, val)):
            #     if key % i == 0:
            #         if val % i == 0:
            #             d_nums[key] = d_nums.get(key, []) + [val]
    for strng in d_nums:
        print(f'{strng} - {d_nums[strng][:-2]}')
    # print()

    # for _ in range(int(input())):
    #     name, str = input().split(': ')
    #     toys.extend(set(str.split(', ')))
    #
    # for i in range(len(toys)):
    #     toy = toys.pop(0)
    #     if toy not in toys:
    #         unique.append(toy)
    #     toys.append(toy)


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    simple_task_4()


if __name__ == '__main__':
    main()
