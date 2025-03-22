import math
from collections import defaultdict


def find_minimal_product_sum_numbers(max_k):
    minimal_numbers = {}

    def dfs(current_product, current_sum, count, start):
        if current_product > 2 * max_k:
            return
        if count >= 2:
            k = current_product - current_sum + count
            if 2 <= k <= max_k:
                if k not in minimal_numbers or current_product < minimal_numbers[k]:
                    minimal_numbers[k] = current_product
        for i in range(start, max_k // current_product + 1):
            dfs(current_product * i, current_sum + i, count + 1, i)

    dfs(1, 0, 0, 2)
    return minimal_numbers


def sum_minimal_product_sum_numbers(max_k):
    minimal_numbers = find_minimal_product_sum_numbers(max_k)
    unique_numbers = set(minimal_numbers.values())
    return sum(unique_numbers)


max_k = 12000
result = sum_minimal_product_sum_numbers(max_k)

print(f"The sum of all minimal product-sum numbers for 2 <= k <= 12000 is: {result}")