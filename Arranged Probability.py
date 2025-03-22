import math


def find_minimal_blue_discs():
    # Initial solution (b, n) = (15, 21)
    b = 15
    n = 21

    # Recurrence relations for Pell's equation
    # b_{k+1} = 3*b_k + 2*n_k - 2
    # n_{k+1} = 4*b_k + 3*n_k - 3

    while n <= 10 ** 12:
        b_new = 3 * b + 2 * n - 2
        n_new = 4 * b + 3 * n - 3
        b, n = b_new, n_new

    return b


# Find the number of blue discs in the first arrangement with over 10^12 discs
result = find_minimal_blue_discs()

print(f"The number of blue discs is: {result}")