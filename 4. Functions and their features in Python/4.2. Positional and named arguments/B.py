def make_matrix(size: int | tuple, value=0) -> list:
    if isinstance(size, int):
        size = [size, size]
    # array = [[0] * n for i in range(n)]
    # print([[value] * size[0] for i in range(size[1])])
    return [[value] * size[0] for i in range(size[1])]


# make_matrix(3)
assert make_matrix(3) == [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
assert make_matrix((4, 2), 1) == [
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]
