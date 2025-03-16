def digital_sum(n):
    # Calculate the sum of the digits of n
    return sum(int(digit) for digit in str(n))

def max_digital_sum():
    max_sum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            power = a ** b
            current_sum = digital_sum(power)
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum

result = max_digital_sum()

print(f"The maximum digital sum is: {result}")