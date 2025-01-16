import datetime

now = datetime.datetime.now()

#now is basically a class with attributes
print(now)
print(type(now))
print(now.year)
date = datetime.date(2023, 6, 14) #format
hours = datetime.time(14, 29, 1)

print(datetime.datetime(2023, 12, 31, 23, 59, 59, 999))
print(hours)
print(date)