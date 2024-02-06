def is_palindrome(test):
    """А роза упала на лапу Азора 7.0"""
    if isinstance(test, int) or isinstance(test, float):
        test = str(abs(test))
    return test == test[::-1]


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
