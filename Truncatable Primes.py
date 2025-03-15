def sieve_of_eratosthenes(limit):
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False

    for p in range(2, int(limit ** 0.5) + 1):
        if prime[p]:
            for i in range(p * p, limit + 1, p):
                prime[i] = False

    return prime


def is_truncatable_prime(n, prime):
    s = str(n)
    length = len(s)

    for i in range(length):
        if not prime[int(s[i:])]:
            return False

    for i in range(length, 0, -1):
        if not prime[int(s[:i])]:
            return False

    return True


def sum_truncatable_primes(limit):
    prime = sieve_of_eratosthenes(limit)
    truncatable_primes = []

    for p in range(10, limit):
        if prime[p] and is_truncatable_prime(p, prime):
            truncatable_primes.append(p)

    return sum(truncatable_primes)


limit = 1000000
result = sum_truncatable_primes(limit)

print(f"The sum of all truncatable primes is: {result}")
