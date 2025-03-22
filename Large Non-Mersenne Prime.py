# Calculate 2^7830457 mod 10^10
exponent = 7830457
modulus = 10**10

# Using the built-in pow function with three arguments for efficient modular exponentiation
power_of_two = pow(2, exponent, modulus)

# Multiply by 28433 and add 1, then take modulo 10^10 to get the last ten digits
result = (28433 * power_of_two + 1) % modulus

print(f"The last ten digits of the prime number are: {result:010}")