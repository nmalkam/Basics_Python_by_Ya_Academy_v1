total = wrong = 0
for _ in range(1000):
    for count in range(1, 201):
        nums = [randint(1, 1001) for _ in range(count//10 + 1)]
        total += 1
        if gcd_bench(nums) != gcd_sample(nums):
            wrong += 1
            print(f'данные: {nums=}, ожидали: {gcd_bench(nums)=}, получили: {gcd_sample(nums)=}')  # noqa  # nopep8

print(f'Всего сделано тестов: {total}, ошибок: {wrong}({wrong/total*100:.2f}%)')  # noqa  # nopep8

