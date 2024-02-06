def simple_task_4():  # 2.4. Вложенные циклы K.Простая задача_3 Simple task 3

    def mutually_prime(key_num: int, val_num: int) -> bool:
        for i in range(2, max(key_num, val_num) + 1):
            if key_num % i == 0:
                if val_num % i == 0:
                    return False
        return True

    d_nums = {}

    nums = sorted(map(int, set(sorted(input().split('; ')))))

    for key in nums:
        for val in nums:
            if mutually_prime(key, val):
                d_nums[key] = d_nums.get(key, '') + f'{val}, '

    for strng in sorted(d_nums):
        print(f'{strng} - {d_nums[strng][:-2]}')
    # print()


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    simple_task_4()


if __name__ == '__main__':
    main()
