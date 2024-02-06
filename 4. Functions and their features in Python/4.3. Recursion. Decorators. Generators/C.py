"""Многочлен N-ой степени"""


def make_equation(*nums):
    # print(len(nums))
    a = nums
    print(type(nums))
    if 1 < len(nums):
        # print(nums[:-1])
        # print(f"(DIVE_OUT) * x + {nums[-1]}")
        return f"({make_equation(*nums[:-1])}) * x + {nums[-1]}"
    # else:
    #     # print(f'({nums[0]})')
    return f'{nums[0]}'
# (3) * x + 1


result = make_equation(3, 1, 5, 3)
print(result)
print()
