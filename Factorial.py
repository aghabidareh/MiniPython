def factorial(n):
    n = int(n)
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

print(factorial(5))
print(factorial(10))
print(factorial(100))
print(factorial(1000))