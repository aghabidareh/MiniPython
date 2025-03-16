import sympy


def is_prime(n):
    return sympy.isprime(n)


def find_side_length():
    side_length = 1
    total_diagonals = 1
    prime_count = 0
    current_number = 1

    while True:
        side_length += 2
        for _ in range(4):
            current_number += side_length - 1
            if is_prime(current_number):
                prime_count += 1
        total_diagonals += 4
        ratio = prime_count / total_diagonals
        if ratio < 0.1:
            return side_length


result = find_side_length()

print(f"The side length of the square spiral is: {result}")