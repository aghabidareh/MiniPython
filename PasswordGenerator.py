from random import choice
from string import punctuation, ascii_lowercase, ascii_uppercase, digits


def generator(length=8, usePunctiation=True, useLowerCaseWords=True, useUpperCaseWords=True, useDigits=True):
    string = ''
    if useLowerCaseWords:
        string += ascii_lowercase
    if useUpperCaseWords:
        string += ascii_uppercase
    if useDigits:
        string += digits
    if usePunctiation:
        string += punctuation

    if not string:
        print('no string is there')
        exit()

    password = ''.join(choice(string) for _ in range(length))

    return password


print(generator())
