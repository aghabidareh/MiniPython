from colorama import Fore

print(Fore.GREEN)

second = 60 
secondsInHour = 60 * 60
secondsInDay = 24 * secondsInHour
secondsInWeek = 7 * secondsInDay
secondsInMonth = 4 * secondsInWeek
secondsInYear = 12 * secondsInMonth

print(f'we have {second} in a minute')
print(f'we have {secondsInHour} in an hour')
print(f'we have {secondsInDay} in a day')
print(f'we have {secondsInWeek} in a week')
print(f'we have {secondsInMonth} in a month')
print(f'we have {secondsInYear} in a year')

print()

print(Fore.RED + "let's back to another project!")

print(Fore.WHITE)
