def is_palindrome(arg: str | int | tuple | list | float) -> bool:
    """А роза упала на лапу Азора 7.0"""
    if isinstance(arg, tuple):
        arg = list(str(arg[0]))
    if isinstance(arg, int | float):
        arg = list(str(arg))
    if arg == arg[::-1]:
        return True
    return False


assert is_palindrome(tuple([323])) == True
assert is_palindrome(323.323) == True
assert is_palindrome(tuple([-13231])) == False
assert is_palindrome("323") == True
assert is_palindrome(123) == False
assert is_palindrome([1, 2, 1, 2, 1]) == True
assert is_palindrome([1, 2, -1, 2, 1]) == True
assert is_palindrome([1, -2, -1, -2, 1]) == True
assert is_palindrome([1, 2, -1, -2, 1]) == False
assert is_palindrome([-1, -2, -1, -2, 1]) == False
print(1)
