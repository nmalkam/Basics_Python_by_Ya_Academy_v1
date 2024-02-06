def merge(tuple1: tuple, tuple2: tuple) -> tuple:
    """Слияние
    J_v3(right version, without standard sorting).py"""

    res = []
    t_l1 = list(tuple1)
    t_l2 = list(tuple2)
    while t_l1 and t_l2:
        if t_l1[0] > t_l2[0]:
            res.append(t_l2.pop(0))
        else:
            res.append(t_l1.pop(0))
    if t_l1:

        for i in t_l1:
            res.append(i)
    if t_l2:

        for i in t_l2:
            res.append(i)
    return tuple(res)


assert merge((1, 2), (3, 4, 5)) == (1, 2, 3, 4, 5)
assert merge((7, 12), (1, 9, 50)) == (1, 7, 9, 12, 50)
print('OKAY')
