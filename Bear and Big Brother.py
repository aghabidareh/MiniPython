limak, bob = input().split()
year = 0

limak = int(limak)
bob = int(bob)

while True:

    if bob >= limak:
        year += 1
    else:
        break

    limak *= 3
    bob *= 2

print(year)