import math

def count_fractions_between_one_third_and_one_half(limit):
    count = 0
    for d in range(2, limit + 1):
        lower_bound = d // 3 + 1
        upper_bound = (d - 1) // 2
        for n in range(lower_bound, upper_bound + 1):
            if math.gcd(n, d) == 1:
                count += 1
    return count

# Count the number of fractions between 1/3 and 1/2 for d <= 12,000
limit = 12000
result = count_fractions_between_one_third_and_one_half(limit)

print(f"The number of fractions between 1/3 and 1/2 for d <= 12,000 is: {result}")