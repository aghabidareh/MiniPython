def find_fraction_left_of_three_seventh(limit):
    target_numerator = 3
    target_denominator = 7

    best_numerator = 0
    best_denominator = 1

    for d in range(2, limit + 1):
        n = (3 * d - 1) // 7
        if n * target_denominator < target_numerator * d:
            if n * best_denominator > best_numerator * d:
                best_numerator = n
                best_denominator = d

    return best_numerator


limit = 1000000
result = find_fraction_left_of_three_seventh(limit)

print(f"The numerator of the fraction immediately to the left of 3/7 is: {result}")
