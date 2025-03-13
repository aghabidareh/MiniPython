import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


primes = []
counter = 0
i = 2

while True:
    if isPrime(i):
        counter += 1
        primes.append(i)
    i += 1
    if counter >= 10_001:
        print(primes[-1])
        break
