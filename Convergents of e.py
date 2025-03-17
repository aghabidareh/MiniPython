def compute_e_continued_fraction(n):
    seq = [2]
    for k in range(1, n):
        if k % 3 == 2:
            seq.append(2 * (k // 3 + 1))
        else:
            seq.append(1)
    return seq

def compute_convergent(seq):
    num, denom = 1, 0  # Start from the last term
    for a in reversed(seq):
        num, denom = a * num + denom, num
    return num  # Numerator

# Get the 100th continued fraction sequence for e
e_sequence = compute_e_continued_fraction(100)

numerator_100 = compute_convergent(e_sequence)

sum_digits = sum(int(digit) for digit in str(numerator_100))

print(sum_digits)
