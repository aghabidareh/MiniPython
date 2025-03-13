# Initialize a cache to store sequence lengths
cache = {}


def collatz_sequence_length(n):
    if n in cache:
        return cache[n]
    if n == 1:
        return 1
    if n % 2 == 0:
        length = 1 + collatz_sequence_length(n // 2)
    else:
        length = 1 + collatz_sequence_length(3 * n + 1)
    cache[n] = length
    return length


max_length = 0
starting_number = 0

for i in range(1, 1000000):
    current_length = collatz_sequence_length(i)
    if current_length > max_length:
        max_length = current_length
        starting_number = i

print(starting_number)
