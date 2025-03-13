string = input('enter a string: ')
lists = ['a', 'g', 'h', 'a', 'b', 'i', 'd', 'a', 'r', 'e', 'h']

if string in lists:
    print(string + ' ' + ''.join(lists))
else:
    print(''.join(lists))
