def merge(tuple1: tuple, tuple2: tuple) -> tuple:
    """Слияние"""

    res = []
    index_1 = 0
    index_2 = 0
    while index_1 != len(tuple1) and index_2 != len(tuple2):
        if tuple1[index_1] > tuple2[index_2]:
            res.append(tuple2[index_2])
            index_2 += 1
        else:
            res.append(tuple1[index_1])
            index_1 += 1
    if index_1 == len(tuple1):
        res.extend(tuple2[index_2:])
    elif index_2 == len(tuple2):
        res.extend(tuple1[index_1:])
    return tuple(res)


assert merge((1, 2), (3, 4, 5)) == (1, 2, 3, 4, 5)
assert merge((7, 12), (1, 9, 50)) == (1, 7, 9, 12, 50)
assert merge((1, 91), (3, 4, 90)) == (1, 3, 4, 90, 91)
print('OKAY')
