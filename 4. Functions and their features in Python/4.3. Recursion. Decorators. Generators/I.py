def cycle(args: list):
    while True:
        for arg in args:
            yield arg


print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))
print(*(x for _, x in zip(range(15), cycle([1, 2, 3, 4]))))
def cycl(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element

cycl([123])
