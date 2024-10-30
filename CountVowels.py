counter = 0
string = input("Enter a string: ")
vowels = ['a' , 'o' , 'u' , 'e' , 'i']

for s in string:
    if s in vowels:
        counter += 1

print(f'count of vowels: {counter}')