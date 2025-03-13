import math

factorial_100 = math.factorial(100)

factorial_str = str(factorial_100)

digit_sum = sum(int(digit) for digit in factorial_str)

print(digit_sum)