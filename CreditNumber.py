creditNumber = input("Enter your credit number: ")

if(len(creditNumber) < 16):
    print("Your credit number is invalid.")
    exit()

creditNumber = creditNumber.replace(creditNumber[:-4] , len(creditNumber[:-4]) * '*')

print('your credit number is', creditNumber)