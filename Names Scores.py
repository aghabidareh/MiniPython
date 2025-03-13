# Function to calculate the alphabetical value of a name
def alphabetical_value(name):
    return sum(ord(char) - ord('A') + 1 for char in name)


with open('names.txt', 'r') as file:
    names = file.read().replace('"', '').split(',')

names.sort()

total_score = 0
for index, name in enumerate(names):
    value = alphabetical_value(name)
    score = value * (index + 1)
    total_score += score

print(total_score)
