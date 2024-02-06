"""Рекурсивный сумматор"""
def recursive_sum(*nums):
    while nums[1:]:
        return nums[0] + recursive_sum(*nums[1:])
    return nums[0]

# def recursive_sum(*nums):
#     if not nums:
#         return 0
#     return nums[0] + recursive_sum(*nums[1:])


result = recursive_sum(1, 2, 3)
# # Вызов recursive_sum(1, 2, 3)
# # Вызов recursive_sum(1, 2)
# # Вызов recursive_sum(1)
# # Вызов recursive_sum()
# result = 6
print(result)
print()
