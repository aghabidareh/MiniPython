import itertools
import sympy

def generate_4_digit_primes():
    return [p for p in range(1000, 10000) if sympy.isprime(p)]

def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))

def find_arithmetic_sequence(primes):
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            p1 = primes[i]
            p2 = primes[j]
            difference = p2 - p1
            p3 = p2 + difference
            if p3 in primes and is_permutation(p1, p2) and is_permutation(p2, p3):
                if p1 != 1487:
                    return p1, p2, p3
    return None

primes = generate_4_digit_primes()

sequence = find_arithmetic_sequence(primes)

if sequence:
    result = int(''.join(map(str, sequence)))
    print(f"The 12-digit number formed by concatenating the three terms is: {result}")
else:
    print("No such sequence found.")