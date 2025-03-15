def is_palindrome(s):
    return s == s[::-1]


def is_palindromic_in_both_bases(n):
    if not is_palindrome(str(n)):
        return False

    binary = bin(n)[2:]

    return is_palindrome(binary)


def sum_double_base_palindromes(limit):
    total = 0
    for n in range(1, limit):
        if is_palindromic_in_both_bases(n):
            total += n
    return total


limit = 1000000
result = sum_double_base_palindromes(limit)

print(f"The sum of all numbers less than one million that are palindromic in both base 10 and base 2 is: {result}")
