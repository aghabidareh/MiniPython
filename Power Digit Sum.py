number = 2 ** 1000

number_str = str(number)

digit_sum = sum(int(digit) for digit in number_str)

print(digit_sum)
