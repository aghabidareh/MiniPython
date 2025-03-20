import math
from decimal import Decimal, getcontext

def is_perfect_square(n):
    return int(math.isqrt(n)) ** 2 == n

def sum_first_hundred_digits(n):
    getcontext().prec = 105  # Set precision to ensure 100 decimal digits
    sqrt_n = Decimal(n).sqrt()
    sqrt_str = str(sqrt_n).replace('.', '')  # Remove the decimal point
    return sum(int(digit) for digit in sqrt_str[:100])

def total_digital_sums(limit):
    total = 0
    for n in range(1, limit + 1):
        if not is_perfect_square(n):
            total += sum_first_hundred_digits(n)
    return total

limit = 100
result = total_digital_sums(limit)

print(f"The total of the digital sums is: {result}")