def process_string(string):
    vowels = "aeiou"
    result = []

    for char in string:
        if char not in vowels:
            result.append('.' + char)

    return ''.join(result)