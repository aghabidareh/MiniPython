number = int(input())
c = 0

for _ in range(number):
    operation = input()
    if '--' in operation:
        c -= 1
    elif '++' in operation:
        c += 1
print(c)
