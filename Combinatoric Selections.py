def binomial_coefficient(n, r):
    if r > n - r:
        r = n - r
    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)
    return result


def count_binomial_coefficients_above_one_million():
    count = 0
    for n in range(1, 101):
        for r in range(1, n + 1):
            bc = binomial_coefficient(n, r)
            if bc > 1000000:
                count += 1
    return count


result = count_binomial_coefficients_above_one_million()

print(f"The number of binomial coefficients greater than one million is: {result}")
