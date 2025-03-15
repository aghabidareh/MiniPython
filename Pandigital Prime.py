import itertools
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_largest_pandigital_prime():
    digits = "7654321"
    for perm in itertools.permutations(digits):
        num = int(''.join(perm))
        if is_prime(num):
            return num
    return None

result = find_largest_pandigital_prime()

print(f"The largest pandigital prime is: {result}")