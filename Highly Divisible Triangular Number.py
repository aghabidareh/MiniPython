# find the value of the first triangle number to have over five hundred divisors

def count_divisors(n):
    count = 1
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            exponent = 0
            while n % factor == 0:
                n = n // factor
                exponent += 1
            count *= (exponent + 1)
        factor += 1
    if n > 1:
        count *= 2
    return count


def find_triangle_number_with_divisors(limit):
    n = 1
    while True:
        triangle_number = n * (n + 1) // 2
        divisors = count_divisors(triangle_number)
        if divisors > limit:
            return triangle_number
        n += 1


limit = 500

result = find_triangle_number_with_divisors(limit)

print(f"The first triangle number with over {limit} divisors is: {result}")
