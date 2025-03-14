def sum_of_fifth_powers():
    fifth_powers = {str(d): d ** 5 for d in range(10)}

    total_sum = 0

    for num in range(2, 354295):
        num_str = str(num)
        sum_fifth = sum(fifth_powers[digit] for digit in num_str)
        if sum_fifth == num:
            total_sum += num

    return total_sum


result = sum_of_fifth_powers()
print(f"The sum of all numbers that can be written as the sum of fifth powers of their digits is: {result}")
