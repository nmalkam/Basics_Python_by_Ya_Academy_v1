"""Я НЕ ПОНИМАЮ ЧТО ПРОИСХОДИТ РЕШЕНИЕ С ЗАКОММЕНТИРОВАННЫМИ СТРОКАМИ
ЯНДЕКС ОТКАЗАЛСЯ ПРИНИМАТЬ 12 ТЕСТ НЕ ПРОХОДИЛ"""
# if len(nums) == 1:
#     return nums[0]
def gcd(*nums: int) -> int:
    first = nums[0]
    for num in nums[1:]:
        while first != 0 and num != 0:
            if first >= num:
                first = first % num
            else:
                num = num % first
        first = num + first
    return first


assert gcd(36, 48, 156, 100500) == 12
assert gcd(3) == 3
print('OKAY')
