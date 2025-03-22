
exponent = 7830457
modulus = 10**10

power_of_two = pow(2, exponent, modulus)

result = (28433 * power_of_two + 1) % modulus

print(f"The last ten digits of the prime number are: {result:010}")