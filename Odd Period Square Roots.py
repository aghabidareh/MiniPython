import math


def continued_fraction_period(n):
    """Computes the period of the continued fraction representation of sqrt(n)."""
    sqrt_n = math.isqrt(n)
    if sqrt_n * sqrt_n == n:
        return 0  # Perfect squares have no period

    m, d, a0 = 0, 1, sqrt_n
    a = a0
    period = 0

    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        period += 1
        if a == 2 * a0:  # Repeats when a_n = 2 * a_0
            break

    return period


count = sum(1 for n in range(2, 10001) if continued_fraction_period(n) % 2 == 1)
print(count)
