def sum_of_proper_divisors(n):
    if n < 2:
        return 0
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            if i == n // i:
                total += i
            else:
                total += i + n // i
        i += 1
    return total

def find_abundant_numbers(limit):
    abundant_numbers = []
    for n in range(1, limit + 1):
        if sum_of_proper_divisors(n) > n:
            abundant_numbers.append(n)
    return abundant_numbers

def generate_abundant_sums(abundant_numbers, limit):
    abundant_sums = set()
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            sum_abundant = abundant_numbers[i] + abundant_numbers[j]
            if sum_abundant > limit:
                break
            abundant_sums.add(sum_abundant)
    return abundant_sums

def sum_of_non_abundant_sums(limit):
    abundant_numbers = find_abundant_numbers(limit)
    abundant_sums = generate_abundant_sums(abundant_numbers, limit)
    total = 0
    for n in range(1, limit + 1):
        if n not in abundant_sums:
            total += n
    return total

limit = 28123

result = sum_of_non_abundant_sums(limit)
print(result)