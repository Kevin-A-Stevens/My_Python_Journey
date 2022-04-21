import time
import datetime

print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))
print("The current timezone is {0}  with an offset of {1}".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("\tdaylight Saving Time is in effect for this location")
    print("\tThe DST timezone is " + time.tzname[1])

print("Local time is " + time.strftime('%T-%m-%d %H:%M:%S', time.localtime()))
print("UTC time is " + time.strftime('%T-%m-%d %H:%M:%S', time.gmtime()))

print("-" * 80)
print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
