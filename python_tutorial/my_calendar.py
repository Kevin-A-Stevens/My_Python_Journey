import calendar
import datetime
import time

print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2022, 7))
print()

print(calendar.monthcalendar(2022, 7))
print()

print(calendar.calendar(2022))
print()

day_of_the_week = calendar.weekday(2022, 7, 31)
print(day_of_the_week)

is_leap = calendar.isleap(2022)
print(is_leap)

how_many_leap_days = calendar.leapdays(2000, 3000)
print(how_many_leap_days)


