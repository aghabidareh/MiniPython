import math

def find_max_line(file_path):
    max_value = -1
    max_line = 0
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            base, exp = map(int, line.strip().split(','))
            log_value = exp * math.log(base)
            if log_value > max_value:
                max_value = log_value
                max_line = line_number
    return max_line

# Find the line number with the greatest numerical value
file_path = '0099_base_exp.txt'
result = find_max_line(file_path)

print(f"The line number with the greatest numerical value is: {result}")