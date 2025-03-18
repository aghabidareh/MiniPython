def compute_totients(limit):
    phi = list(range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:  # p is prime
            for multiple in range(p, limit + 1, p):
                phi[multiple] -= phi[multiple] // p
    return phi


def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))


def find_min_ratio_n(limit):
    phi = compute_totients(limit)
    min_ratio = float('inf')
    result_n = 0
    for n in range(2, limit):
        if is_permutation(n, phi[n]):
            ratio = n / phi[n]
            if ratio < min_ratio:
                min_ratio = ratio
                result_n = n
    return result_n


limit = 10 ** 7
result = find_min_ratio_n(limit)

print(f"The value of n < 10^7 for which phi(n) is a permutation of n and n/phi(n) is minimized is: {result}")
