
heartBeatInEveryMinute = 72
breathInEveryMinute = 30

birthYear = int(input("Enter Your Birth Year: "))
toYears = 2024

age = toYears - birthYear

MonthYouLive = 12 * age
DaysYouLive = 30 * MonthYouLive
HoursYouLive = 24 * DaysYouLive
MinutesYouLive = 60 * HoursYouLive

BeatHeartes = heartBeatInEveryMinute * MinutesYouLive
Breathes = breathInEveryMinute * MinutesYouLive

print(f'Your Heart Beates in {age} is {BeatHeartes}')
print(f'Your Breathes in {age} is {Breathes}')