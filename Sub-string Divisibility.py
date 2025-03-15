import itertools


def is_pandigital(number):
    digits = set(str(number))
    return len(digits) == 10 and len(str(number)) == 10


def satisfies_conditions(number):
    s = str(number)
    divisors = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        substring = int(s[i:i + 3])
        if substring % divisors[i - 1] != 0:
            return False
    return True


def find_pandigital_numbers():
    digits = "0123456789"
    pandigital_numbers = [''.join(p) for p in itertools.permutations(digits) if p[0] != '0']

    valid_numbers = [int(num) for num in pandigital_numbers if satisfies_conditions(num)]
    return valid_numbers


valid_numbers = find_pandigital_numbers()

result = sum(valid_numbers)

print(f"The sum of all 0 to 9 pandigital numbers with the property is: {result}")
