def recurring_cycle_length(d):
    if d % 2 == 0 or d % 5 == 0:
        return 0

    remainder = 1
    position = 0
    while True:
        remainder = (remainder * 10) % d
        position += 1
        if remainder == 1:
            return position
        if remainder == 0:
            return 0


def find_longest_recurring_cycle(limit):
    max_length = 0
    best_d = 0

    for d in range(2, limit):
        cycle_length = recurring_cycle_length(d)
        if cycle_length > max_length:
            max_length = cycle_length
            best_d = d

    return best_d, max_length


limit = 1000
best_d, max_length = find_longest_recurring_cycle(limit)
print(f"The value of d < {limit} with the longest recurring cycle is {best_d} with a cycle length of {max_length}.")
