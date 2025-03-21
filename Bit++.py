number = int(input())
result = 0

for _ in range(number):
    operation = input()
    if '--' in operation:
        result -= 1
    elif '++' in operation:
        result += 1
print(result)
