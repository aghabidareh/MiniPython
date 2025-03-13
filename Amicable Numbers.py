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

def find_amicable_numbers(limit):
    amicable_numbers = set()
    for a in range(2, limit):
        b = sum_of_proper_divisors(a)
        if b > a and sum_of_proper_divisors(b) == a:
            amicable_numbers.add(a)
            amicable_numbers.add(b)
    return sum(amicable_numbers)

result = find_amicable_numbers(10000)
print(result)