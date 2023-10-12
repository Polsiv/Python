import time
from datetime import datetime
"""
#returns time in seconds since epoch dec 31 1969 / 6:00pm
print(time.time())

#returns current time
print(time.ctime(time.time()))

time_object = time.localtime()
print(time_object) 

print()
"""


def str_to_hour(input_str):
    datetime_object = datetime.strptime(input_str, '%H:%M:%S')
    return datetime_object.strftime('%H:%M:%S')

input_str = '13:45:30'
hour_str = str_to_hour(input_str)
print(hour_str) 
# Output: '13:45:30' # Output: '13:45:00'

time_obj = time.localtime()
current_time = time.strftime("%X", time_obj)

print(current_time)

# if current_time > hour_str:
#     print("clock is ahead of time")
