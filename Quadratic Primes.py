import random


def is_prime(n, k=5):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13]:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randint(2, min(n - 2, 1 << 30))
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def find_max_consecutive_primes():
    max_primes = 0
    best_a, best_b = 0, 0

    for b in range(2, 1001):
        if not is_prime(b):
            continue

        for a in range(-999, 1000):
            n = 0
            while True:
                value = n * n + a * n + b
                if value < 2 or not is_prime(value):
                    break
                n += 1

            if n > max_primes:
                max_primes = n
                best_a, best_b = a, b

    return best_a, best_b, max_primes


best_a, best_b, max_primes = find_max_consecutive_primes()
product = best_a * best_b

print(f"The quadratic expression n^2 + {best_a}n + {best_b} produces {max_primes} consecutive primes.")
print(f"The product of a and b is: {product}")
