import time
import re

def validate_time_format(time_str: str) -> bool:
    pattern = re.compile(r'^([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$')
    return pattern.match(time_str)
        
def comparar_hora(input_time: str) -> bool:
    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min

    # Calculate the time 1 hour ahead of the current time
    one_hour_later = current_hour + 1
    if one_hour_later >= 24:
        one_hour_later -= 24

    one_hour_later_str = f'{one_hour_later:02}:{current_minute:02}:00'

    # Compare the input time with the time 1 hour ahead
    return input_time >= one_hour_later_str

HoraSalida = input("Enter a departure time (HH:MM:SS): ")

while not (validate_time_format(HoraSalida) and comparar_hora(HoraSalida)):
    HoraSalida = input("Please enter a valid time at least 1 hour ahead of the current time (HH:MM:SS): ")


