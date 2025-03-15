def is_pentagonal(x):
    n = (1 + (1 + 24 * x) ** 0.5) / 6
    return n == int(n)

def find_next_tri_pent_hex():
    n = 144
    while True:
        H_n = n * (2 * n - 1)
        if is_pentagonal(H_n):
            return H_n
        n += 1

result = find_next_tri_pent_hex()

print(f"The next triangle number that is also pentagonal and hexagonal is: {result}")