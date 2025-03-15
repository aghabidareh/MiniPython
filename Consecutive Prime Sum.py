
def sieve_of_eratosthenes(limit):
    # Generate all prime numbers below the limit using the Sieve of Eratosthenes
    sieve = [True] * (limit)
    sieve[0] = sieve[1] = False
    for p in range(2, int(limit ** 0.5) + 1):
        if sieve[p]:
            for i in range(p * p, limit, p):
                sieve[i] = False
    return [p for p, is_prime in enumerate(sieve) if is_prime]


def find_longest_consecutive_prime_sum(primes, limit):
    max_length = 0
    result_prime = 0
    primes_set = set(primes)

    for i in range(len(primes)):
        sum_primes = 0
        current_length = 0
        for j in range(i, len(primes)):
            sum_primes += primes[j]
            current_length += 1
            if sum_primes >= limit:
                break
            if sum_primes in primes_set and current_length > max_length:
                max_length = current_length
                result_prime = sum_primes
    return result_prime, max_length


limit = 1000000
primes = sieve_of_eratosthenes(limit)

result_prime, max_length = find_longest_consecutive_prime_sum(primes, limit)

print(f"The prime below one million that can be written as the sum of the most consecutive primes is: {result_prime}")
print(f"It is the sum of {max_length} consecutive primes.")