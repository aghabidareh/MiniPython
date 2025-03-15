from math import gcd
from functools import reduce


def simplify_fraction(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor


def find_curious_fractions():
    fractions = []

    for a in range(10, 100):
        for b in range(a + 1, 100):
            if a % 10 == 0 and b % 10 == 0:
                continue

            a_str = str(a)
            b_str = str(b)

            common_digits = set(a_str).intersection(set(b_str))
            if not common_digits:
                continue

            for digit in common_digits:
                new_a = int(a_str.replace(digit, "", 1))
                new_b = int(b_str.replace(digit, "", 1))

                # Avoid division by zero
                if new_b == 0:
                    continue

                if new_a / new_b == a / b:
                    fractions.append((a, b))
                    break

    return fractions


def compute_product(fractions):
    numerator = 1
    denominator = 1
    for a, b in fractions:
        numerator *= a
        denominator *= b

    simplified_numerator, simplified_denominator = simplify_fraction(numerator, denominator)
    return simplified_denominator


curious_fractions = find_curious_fractions()

result = compute_product(curious_fractions)

print(f"The denominator of the product in lowest terms is: {result}")
