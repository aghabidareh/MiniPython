def find_least_n_divisible_by_one_million():
    target = 1000000
    p = [0] * (10**6)  # Adjust the size if necessary
    p[0] = 1
    n = 1
    while True:
        i = 1
        pentagonal = 1
        p_n = 0
        while pentagonal <= n:
            sign = (-1) ** (i - 1)
            p_n += sign * p[n - pentagonal]
            i += 1
            # Generate the next pentagonal number
            k = (i // 2) + 1 if i % 2 == 0 else -(i // 2) - 1
            pentagonal = k * (3 * k - 1) // 2
        p[n] = p_n % target
        if p[n] == 0:
            return n
        n += 1

# Find the least value of n for which p(n) is divisible by one million
result = find_least_n_divisible_by_one_million()

print(f"The least value of n for which p(n) is divisible by one million is: {result}")