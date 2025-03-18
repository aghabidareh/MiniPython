import itertools

def is_magic_5gon(external, internal):
    # Check if the 5-gon ring is magic
    total = external[0] + internal[0] + internal[1]
    for i in range(1, 5):
        if external[i] + internal[i] + internal[(i + 1) % 5] != total:
            return False
    return True

def form_16_digit_string(external, internal):
    # Form the 16-digit string starting from the smallest external node
    start_index = external.index(min(external))
    result = []
    for i in range(5):
        idx = (start_index + i) % 5
        result.append(str(external[idx]))
        result.append(str(internal[idx]))
        result.append(str(internal[(idx + 1) % 5]))
    return ''.join(result)

def find_max_16_digit_string():
    numbers = list(range(1, 11))
    max_string = ''
    for perm in itertools.permutations(numbers):
        external = list(perm[:5])
        internal = list(perm[5:])
        if is_magic_5gon(external, internal):
            current_string = form_16_digit_string(external, internal)
            if len(current_string) == 16 and current_string > max_string:
                max_string = current_string
    return max_string

result = find_max_16_digit_string()

print(f"The maximum 16-digit string for a magic 5-gon ring is: {result}")