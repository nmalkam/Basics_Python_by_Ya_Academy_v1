def make_linear(iterable: list):
    res = []
    for item in iterable:
        if isinstance(item, list):
            pull_out = make_linear(item)
            res.extend(pull_out)
        else:
            res.append(item)
    return res


result = make_linear([1, 2, [3]])
print(result)
result = make_linear([1, [2, [3, 4]], 5, 6])
print(result)
