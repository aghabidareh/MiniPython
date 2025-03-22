def find_minimal_blue_discs():
    b = 15
    n = 21

    while n <= 10 ** 12:
        b_new = 3 * b + 2 * n - 2
        n_new = 4 * b + 3 * n - 3
        b, n = b_new, n_new

    return b


result = find_minimal_blue_discs()

print(f"The number of blue discs is: {result}")
