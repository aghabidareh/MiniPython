limak, bob = map(int, input().split())
year = 0

while True:

    if bob >= limak:
        year += 1
    else:
        break

    limak *= 3
    bob *= 2

print(year)
