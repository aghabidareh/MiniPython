import sympy


def count_distinct_prime_factors(n):
    return len(sympy.factorint(n))


def find_first_four_consecutive():
    n = 1
    while True:
        if all(count_distinct_prime_factors(n + i) == 4 for i in range(4)):
            return n
        n += 1


result = find_first_four_consecutive()

print(f"The first of the four consecutive integers with four distinct prime factors is: {result}")
