def is_palindrome(n):
    # Check if a number is a palindrome
    return str(n) == str(n)[::-1]

def reverse_and_add(n):
    # Reverse the number and add it to the original
    return n + int(str(n)[::-1])

def is_lychrel(n):
    # Check if a number is a Lychrel number within 50 iterations
    for _ in range(50):
        n = reverse_and_add(n)
        if is_palindrome(n):
            return False
    return True

def count_lychrel_numbers(limit):
    # Count the number of Lychrel numbers below the limit
    count = 0
    for n in range(1, limit):
        if is_lychrel(n):
            count += 1
    return count

# Count the number of Lychrel numbers below ten thousand
limit = 10000
result = count_lychrel_numbers(limit)

print(f"The number of Lychrel numbers below ten thousand is: {result}")