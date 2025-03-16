def count_fractions_with_more_digits_in_numerator():
    N_prev_prev, D_prev_prev = 1, 1
    N_prev, D_prev = 3, 2
    count = 0

    for _ in range(2, 1001):
        N_current = 2 * N_prev + N_prev_prev
        D_current = 2 * D_prev + D_prev_prev

        if len(str(N_current)) > len(str(D_current)):
            count += 1

        N_prev_prev, D_prev_prev = N_prev, D_prev
        N_prev, D_prev = N_current, D_current

    return count


result = count_fractions_with_more_digits_in_numerator()

print(f"The number of fractions with more digits in the numerator is: {result}")