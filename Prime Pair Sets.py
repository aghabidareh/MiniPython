import itertools
import sympy

def generate_primes(limit):
    # Generate all prime numbers below the limit
    return [p for p in range(2, limit) if sympy.isprime(p)]

def is_concatenation_prime(p1, p2):
    # Check if both concatenations of p1 and p2 are prime
    concat1 = int(f"{p1}{p2}")
    concat2 = int(f"{p2}{p1}")
    return sympy.isprime(concat1) and sympy.isprime(concat2)

def find_lowest_sum_set(primes):
    # Iterate through all combinations of five primes
    for combination in itertools.combinations(primes, 5):
        valid = True
        for pair in itertools.combinations(combination, 2):
            if not is_concatenation_prime(pair[0], pair[1]):
                valid = False
                break
        if valid:
            return combination, sum(combination)
    return None, None

# Generate a list of primes up to a reasonable limit
primes = generate_primes(10000)

# Find the set of five primes with the lowest sum that satisfies the concatenation property
combination, lowest_sum = find_lowest_sum_set(primes)

if combination:
    print(f"The set of five primes is: {combination}")
    print(f"The lowest sum is: {lowest_sum}")
else:
    print("No such set of five primes found.")