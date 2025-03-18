import math
from sympy import sqrt, Rational, continued_fraction, continued_fraction_convergents

def is_square(n):
    return int(math.isqrt(n)) ** 2 == n

def find_minimal_solution(D):
    if is_square(D):
        return None
    sqrt_D = sqrt(D)
    cf = continued_fraction(sqrt_D)
    convergents = list(continued_fraction_convergents(cf))
    for conv in convergents:
        x, y = conv.numerator, conv.denominator
        if x * x - D * y * y == 1:
            return x, y
    return None

def find_max_x_D(limit):
    max_x = 0
    best_D = 0
    for D in range(2, limit + 1):
        if is_square(D):
            continue
        solution = find_minimal_solution(D)
        if solution:
            x, y = solution
            if x > max_x:
                max_x = x
                best_D = D
    return best_D

limit = 1000
result = find_max_x_D(limit)

print(f"The value of D <= 1000 with the largest minimal x is: {result}")