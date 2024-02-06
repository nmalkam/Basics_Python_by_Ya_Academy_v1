def merge(tuple1: tuple, tuple2: tuple) -> tuple:
    """Слияние"""
    from operator import itemgetter
    lists = [i for i in tuple1]
    lists.extend([i for i in tuple2])
    sorted_list = []
    # for i in lists:
    #     min_list = min(lists)
    #     sorted_list.append(min_list)
    #     lists.pop()
    tuple_out = tuple(lists)
    return tuple_out


assert merge((1, 2), (3, 4, 5)) == (1, 2, 3, 4, 5)
assert merge((7, 12), (1, 9, 50)) == (1, 7, 9, 12, 50)
# assert merge(4) == False
# assert merge(79701) == False
# assert merge(1001459) == True
print('OKAY')
