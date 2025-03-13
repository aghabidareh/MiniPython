def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2 , int(limit ** 0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False

    return [p for p, prime in enumerate(is_prime) if prime]

limit = 2000000

primes = sieve_of_eratosthenes(limit)

sum_of_primes = sum(primes)

print(f"The sum of all primes below {limit} is: {sum_of_primes}")