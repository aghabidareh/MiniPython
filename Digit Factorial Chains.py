import math

factorials = [math.factorial(i) for i in range(10)]


def sum_factorial_digits(n):
    return sum(factorials[int(d)] for d in str(n))


def chain_length(n, memo):
    if n in memo:
        return memo[n]
    seen = {}
    current = n
    length = 0
    while current not in seen:
        seen[current] = length
        current = sum_factorial_digits(current)
        length += 1
    memo[n] = length
    return length


def count_chains_with_60_terms(limit):
    memo = {}
    count = 0
    for n in range(1, limit):
        if chain_length(n, memo) == 60:
            count += 1
    return count


limit = 1000000
result = count_chains_with_60_terms(limit)

print(f"The number of chains with exactly 60 non-repeating terms is: {result}")
