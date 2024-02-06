def make_list(length: int, value=0) -> list:
    # print([value for i in range(length)])
    return [value for i in range(length)]


assert make_list(3) == [0, 0, 0]
assert make_list(5, 1) == [1, 1, 1, 1, 1]
