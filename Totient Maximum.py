import sympy

def find_optimal_n(limit):
    primes = list(sympy.primerange(1, limit))
    n = 1
    for p in primes:
        if n * p > limit:
            break
        n *= p
    return n

limit = 1000000
result = find_optimal_n(limit)

print(f"The value of n <= 1,000,000 for which n / phi(n) is maximized is: {result}")