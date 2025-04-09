def process_string(input_string):
    vowels = "aoyeuiAOYEUI"
    result = []

    for char in input_string:
        if char not in vowels:
            result.append('.' + char.lower())

    return ''.join(result)


input_string = input().strip()
output_string = process_string(input_string)
print(output_string)
