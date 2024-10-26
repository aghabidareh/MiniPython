import math
import numpy as np

def isPrime(n):
    for i in range(2 , int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primeNumbers = np.array([])

for i in range(1_000_000):
    if isPrime(i):
        primeNumbers = np.append(primeNumbers, i)

print(f"the largest prime number is {int(np.max(primeNumbers))}")