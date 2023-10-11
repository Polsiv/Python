import re

def validate_time_format(time_str):
    """
    This function takes in a time string and validates that it is in the format HH:MM:SS using regex.
    """
    pattern = re.compile(r'^([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$')
    if pattern.match(time_str):
        return True
    else:
        return False
    

x = str(input("elpepe xd:"))

print(validate_time_format(x))