def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            for i in range(p*p, limit + 1, p):
                sieve[i] = False
    primes = [p for p, is_prime in enumerate(sieve) if is_prime]
    return primes

def count_prime_sums(limit, target):
    primes = sieve_of_eratosthenes(limit)
    dp = [0] * (limit + 1)
    dp[0] = 1
    for p in primes:
        for i in range(p, limit + 1):
            dp[i] += dp[i - p]
    for i in range(2, limit + 1):
        if dp[i] > target:
            return i
    return -1

limit = 100000
target = 5000
result = count_prime_sums(limit, target)

print(f"The first value which can be written as the sum of primes in over 5,000 different ways is: {result}")