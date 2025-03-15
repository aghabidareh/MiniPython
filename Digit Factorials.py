import math


def sum_of_factorial_of_digits(n):
    return sum(math.factorial(int(digit)) for digit in str(n))


def find_factorions():
    factorions = []

    factorial = [math.factorial(i) for i in range(10)]

    upper_limit = 7 * factorial[9]

    for num in range(10, upper_limit + 1):
        if num == sum_of_factorial_of_digits(num):
            factorions.append(num)

    return factorions


factorions = find_factorions()

result = sum(factorions)

print(f"The sum of all numbers equal to the sum of the factorial of their digits is: {result}")
