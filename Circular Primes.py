def sieve_of_eratosthenes(limit):
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False

    for p in range(2, int(limit ** 0.5) + 1):
        if prime[p]:
            for i in range(p * p, limit + 1, p):
                prime[i] = False

    return prime


def generate_rotations(n):
    s = str(n)
    return [int(s[i:] + s[:i]) for i in range(len(s))]


def count_circular_primes(limit):
    prime = sieve_of_eratosthenes(limit)
    circular_primes = []

    for p in range(2, limit):
        if prime[p]:
            rotations = generate_rotations(p)
            if all(prime[r] for r in rotations):
                circular_primes.append(p)

    return len(circular_primes)


limit = 1000000
result = count_circular_primes(limit)

print(f"The number of circular primes below one million is: {result}")
