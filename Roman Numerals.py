def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in s[::-1]:
        value = roman[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

def count_characters_saved(file_path):
    total_saved = 0
    with open(file_path, 'r') as file:
        for line in file:
            original = line.strip()
            num = roman_to_int(original)
            minimal = int_to_roman(num)
            saved = len(original) - len(minimal)
            total_saved += saved
    return total_saved

file_path = '0089_roman.txt'
result = count_characters_saved(file_path)

print(f"The number of characters saved is: {result}")