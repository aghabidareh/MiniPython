import math


def find_lexicographic_permutation(digits, target):
    permutation = []
    target -= 1
    while digits:
        n = len(digits)
        factorial = math.factorial(n - 1)
        index = target // factorial
        permutation.append(digits.pop(index))
        target %= factorial
    return ''.join(permutation)


digits = [str(i) for i in range(10)]

result = find_lexicographic_permutation(digits, 1000000)
print(result)
