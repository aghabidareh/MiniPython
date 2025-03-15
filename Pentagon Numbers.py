def is_pentagonal(x):
    n = (1 + (1 + 24 * x) ** 0.5) / 6
    return n == int(n)


def generate_pentagonal_numbers(limit):
    pentagonal_numbers = []
    n = 1
    while True:
        p_n = n * (3 * n - 1) // 2
        if p_n > limit:
            break
        pentagonal_numbers.append(p_n)
        n += 1
    return pentagonal_numbers


def find_minimal_difference():
    pentagonal_numbers = []
    n = 1
    while True:
        p_n = n * (3 * n - 1) // 2
        pentagonal_numbers.append(p_n)
        for p_k in pentagonal_numbers[:-1]:
            sum_p = p_n + p_k
            diff_p = abs(p_n - p_k)
            if is_pentagonal(sum_p) and is_pentagonal(diff_p):
                return diff_p
        n += 1


result = find_minimal_difference()

print(f"The minimal difference D is: {result}")
