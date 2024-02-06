def is_prime(n: int) -> bool:
    """Простая задача 5.0"""
    # prime = True
    if n == 1:
        return False
    for i in range(2, int((n + 3) / 2)):
        # if i <= n ** 0.5:  # and prime == True:
        if n % i == 0:
            # prime = False
            return False
    return True

# def is_prime(num):
#     if num == 1:
#         return "NO"
#     for i in range(2, (num // 2) + 1):
#         if num % i == 0:
#             return "NO"
#     return "YES"

assert is_prime(2) == True
assert is_prime(5) == True
assert is_prime(4) == False
assert is_prime(79701) == False
assert is_prime(1001459) == True
print('OKAY')
