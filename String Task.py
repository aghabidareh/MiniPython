def process_string(input_string):
    vowels = "aoyeuiAOYEUI"  # Define the vowels
    result = []  # List to store the processed characters

    for char in input_string:
        if char not in vowels:  # Check if the character is not a vowel
            result.append('.' + char.lower())  # Convert to lowercase and prepend '.'

    return ''.join(result)  # Join the list into a single string

# Example usage:
input_string = input().strip()  # Read the input string
output_string = process_string(input_string)  # Process the string
print(output_string)  # Print the result