import math


def count_n_digit_nth_powers():
    count = 0
    n = 1
    while True:
        lower_bound = 10 ** ((n - 1) / n)
        if lower_bound > 9:
            break
        a_min = math.ceil(lower_bound)
        a_max = 9
        count += (a_max - a_min + 1)
        n += 1
    return count


result = count_n_digit_nth_powers()

print(f"The number of n-digit positive integers which are also nth powers is: {result}")
