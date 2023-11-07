import time
"""import re

def validate_time_format(time_str: str) -> bool:
    pattern = re.compile(r'^([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$')
    return pattern.match(time_str)

def compare_times(input_time: str) -> bool:
    current_time = time.strftime("%H:%M:%S", time.localtime())
    return input_time == current_time

HoraSalida = input("Enter a departure time (HH:MM:SS): ")

while not validate_time_format(HoraSalida):
    HoraSalida = input("Please enter a valid time (HH:MM:SS): ")

print("Waiting for the specified time...")

while not compare_times(HoraSalida):
    time.sleep(1)  # Sleep for 1 second to avoid busy-waiting

print("The specified time has been reached.")

"""

print("first")
time.sleep(10)
print("second")