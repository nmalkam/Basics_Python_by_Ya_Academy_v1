"""Рекурсивный сумматор цифр"""


def recursive_digit_sum(*nums):
    nums = [int(x) for x in str(nums) if x.isdigit()]
    if not nums:
        return 0
    return nums[0] + recursive_digit_sum(nums[1:])


result = recursive_digit_sum(7321346)
print(result)
print()
