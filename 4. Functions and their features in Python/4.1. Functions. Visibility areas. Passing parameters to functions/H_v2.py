def is_palindrome(arg: str | int | tuple | list) -> bool:
    """А роза упала на лапу Азора 7.0"""
    # if isinstance(arg, tuple):
    #     arg = str(arg[0])
    if isinstance(arg, int):
        arg = str(arg)
    return arg == arg[::-1]


assert is_palindrome(-13231, ) == False
# assert is_palindrome(tuple(-13231)) == False
assert is_palindrome(323, ) == True
assert is_palindrome(-11) == False
# assert is_palindrome(323.323) == True
assert is_palindrome(-13231, ) == False
assert is_palindrome("323") == True
assert is_palindrome(123) == False
assert is_palindrome([1, 2, 1, 2, 1]) == True
assert is_palindrome([1, 2, -1, 2, 1]) == True
assert is_palindrome([1, -2, -1, -2, 1]) == True
assert is_palindrome([1, 2, -1, -2, 1]) == False
assert is_palindrome([-1, -2, -1, -2, 1]) == False
print(1)
