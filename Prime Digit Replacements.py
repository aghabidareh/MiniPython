import itertools
import sympy

def sieve_of_eratosthenes(limit):
    # Generate all prime numbers below the limit using the Sieve of Eratosthenes
    sieve = [True] * (limit)
    sieve[0] = sieve[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            for i in range(p*p, limit, p):
                sieve[i] = False
    return [p for p, is_prime in enumerate(sieve) if is_prime]

def replace_digits(n, positions):
    # Replace digits at specified positions with the same digit (0-9)
    s = list(str(n))
    family = []
    for d in '0123456789':
        for pos in positions:
            s[pos] = d
        if s[0] != '0':  # Ensure the number does not start with 0
            family.append(int(''.join(s)))
    return family

def find_smallest_prime_with_eight_prime_family(primes):
    for p in primes:
        s = str(p)
        length = len(s)
        for r in range(1, length):
            for positions in itertools.combinations(range(length), r):
                family = replace_digits(p, positions)
                # Count the number of primes in the family
                prime_count = sum(1 for num in family if sympy.isprime(num))
                if prime_count >= 8:
                    return p
    return None

limit = 1000000
primes = sieve_of_eratosthenes(limit)

result = find_smallest_prime_with_eight_prime_family(primes)

print(f"The smallest prime with an eight prime value family is: {result}")