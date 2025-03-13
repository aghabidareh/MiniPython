# Define letter counts for basic numbers
units = ["one", "two", "three", "four", "five",
         "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
         "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"]

def number_to_letters(n):
    if n == 1000:
        return len("onethousand")
    elif n >= 100:
        hundred_part = units[n // 100 - 1] + "hundred"
        remainder = n % 100
        if remainder == 0:
            return len(hundred_part)
        else:
            return len(hundred_part + "and") + number_to_letters(remainder)
    elif n >= 20:
        ten_part = tens[n // 10 - 2]
        unit_part = units[n % 10 - 1] if n % 10 != 0 else ""
        return len(ten_part + unit_part)
    elif n >= 10:
        return len(teens[n - 10])
    else:
        return len(units[n - 1])

total_letters = sum(number_to_letters(i) for i in range(1, 1001))

print(total_letters)