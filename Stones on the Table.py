num_char, characters = int(input()), input()
counter = 0

for i in range(num_char - 1):
    if characters[i] == characters[i + 1]:
        counter += 1

print(counter)
