def gcd(first, second):
    while first != 0 and second != 0:
        if first > second:
            first = first % second
        else:
            second = second % first
    return second + first
