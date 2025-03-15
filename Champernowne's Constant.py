def construct_fraction(limit):
    fraction = ""
    num = 1
    while len(fraction) < limit:
        fraction += str(num)
        num += 1
    return fraction

def get_digits(fraction, positions):
    digits = []
    for pos in positions:
        digits.append(int(fraction[pos - 1]))
    return digits

def calculate_product(digits):
    product = 1
    for digit in digits:
        product *= digit
    return product

positions = [1, 10, 100, 1000, 10000, 100000, 1000000]

limit = max(positions)
fraction = construct_fraction(limit)

digits = get_digits(fraction, positions)

result = calculate_product(digits)

print(f"The value of the expression is: {result}")