def compute_totients(limit):
    phi = list(range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:  # p is prime
            for multiple in range(p, limit + 1, p):
                phi[multiple] -= phi[multiple] // p
    return phi

def count_reduced_proper_fractions(limit):
    phi = compute_totients(limit)
    return sum(phi[2:limit + 1])

limit = 1000000
result = count_reduced_proper_fractions(limit)

print(f"The number of reduced proper fractions for d <= 1,000,000 is: {result}")