def split_numbers(nums: str) -> tuple:
    # print(tuple([int(num) for num in nums.split()]))
    return tuple([int(num) for num in nums.split()])
split_numbers("1 2 3 4 5")
