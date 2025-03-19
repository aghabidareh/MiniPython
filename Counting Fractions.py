def compute_totients(limit):
    # Initialize a list to store the totient values
    phi = list(range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:  # p is prime
            for multiple in range(p, limit + 1, p):
                phi[multiple] -= phi[multiple] // p
    return phi

def count_reduced_proper_fractions(limit):
    phi = compute_totients(limit)
    # Sum phi(d) for d from 2 to limit
    return sum(phi[2:limit + 1])

# Count the number of reduced proper fractions for d <= 1,000,000
limit = 1000000
result = count_reduced_proper_fractions(limit)

print(f"The number of reduced proper fractions for d <= 1,000,000 is: {result}")