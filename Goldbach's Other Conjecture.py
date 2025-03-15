import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_odd_composite(n):
    return n > 1 and n % 2 != 0 and not is_prime(n)


def can_be_expressed(n, primes):
    for p in primes:
        if p >= n:
            break
        k_squared = (n - p) / 2
        if k_squared == int(k_squared) and k_squared >= 0:
            k = int(k_squared)
            if k * k == k_squared:
                return True
    return False


def find_smallest_failing_odd_composite():
    primes = []
    n = 9
    while True:
        if is_prime(n):
            primes.append(n)
        elif is_odd_composite(n):
            if not can_be_expressed(n, primes):
                return n
        n += 2


result = find_smallest_failing_odd_composite()

print(f"The smallest odd composite that cannot be written as the sum of a prime and twice a square is: {result}")
