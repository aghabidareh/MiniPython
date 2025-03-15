import math
from collections import defaultdict


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def find_max_solutions_perimeter(limit):
    perimeter_counts = defaultdict(int)

    for m in range(2, int(math.sqrt(limit)) + 1):
        for n in range(1, m):
            if (m + n) % 2 == 1 and gcd(m, n) == 1:
                a = m ** 2 - n ** 2
                b = 2 * m * n
                c = m ** 2 + n ** 2
                p = a + b + c

                k = 1
                while k * p <= limit:
                    perimeter_counts[k * p] += 1
                    k += 1

    max_p = max(perimeter_counts, key=lambda x: perimeter_counts[x])
    return max_p


limit = 1000
result = find_max_solutions_perimeter(limit)

print(f"The perimeter p ≤ 1000 with the maximum number of solutions is: {result}")
