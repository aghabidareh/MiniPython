import sys
import math


def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(math.sqrt(limit)) + 1):
        if sieve[p]:
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
    primes = [p for p, is_prime in enumerate(sieve) if is_prime]
    return primes


def count_numbers_below_limit(limit):
    # Determine the maximum prime needed for squares, cubes, and fourth powers
    max_prime_square = int(math.sqrt(limit)) + 1
    max_prime_cube = int(limit ** (1 / 3)) + 1
    max_prime_fourth = int(limit ** (1 / 4)) + 1

    # Generate all primes up to the maximum required
    primes = sieve_of_eratosthenes(max(max_prime_square, max_prime_cube, max_prime_fourth))

    # Generate squares, cubes, and fourth powers
    squares = [p ** 2 for p in primes if p ** 2 < limit]
    cubes = [p ** 3 for p in primes if p ** 3 < limit]
    fourths = [p ** 4 for p in primes if p ** 4 < limit]

    unique_sums = set()

    for s in squares:
        for c in cubes:
            if s + c >= limit:
                break
            for f in fourths:
                total = s + c + f
                if total < limit:
                    unique_sums.add(total)
                else:
                    break

    return len(unique_sums)


limit = 50000000
result = count_numbers_below_limit(limit)

print(
    f"The number of numbers below fifty million that can be expressed as the sum of a prime square, prime cube, and prime fourth power is: {result}")