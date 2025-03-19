import math
from collections import defaultdict


def count_unique_perimeters(limit):
    perimeter_counts = defaultdict(int)

    for m in range(2, int(math.sqrt(limit / 2)) + 1):
        for n in range(1, m):
            if (m + n) % 2 == 1 and math.gcd(m, n) == 1:
                a = m ** 2 - n ** 2
                b = 2 * m * n
                c = m ** 2 + n ** 2
                perimeter = a + b + c
                if perimeter > limit:
                    continue
                k = 1
                while k * perimeter <= limit:
                    perimeter_counts[k * perimeter] += 1
                    k += 1

    count = 0
    for L in perimeter_counts:
        if perimeter_counts[L] == 1:
            count += 1
    return count


limit = 1500000
result = count_unique_perimeters(limit)

print(f"The number of values of L <= 1,500,000 with exactly one Pythagorean triple is: {result}")
