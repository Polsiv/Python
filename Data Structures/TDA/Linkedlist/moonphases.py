#https://saturncloud.io/blog/understanding-lunar-phases-a-guide-for-data-scientists/
#source

def calculate_jdn(year, month, day):
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    jdn = day + ((153 * m + 2) // 5) + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    return jdn
    
jdn = calculate_jdn(2023, 9, 12)
   


def calculate_lunar_phase(jdn):
    new_moon_jdn = 2451550.1  # Known New Moon JDN, e.g., January 6, 2000
    lunar_cycle = 29.53  # Average length of a lunar cycle in days

    days_since_new_moon = jdn - new_moon_jdn
    lunar_phase = (days_since_new_moon % lunar_cycle) / lunar_cycle * 8
    rounded_phase = round(lunar_phase)

    return rounded_phase

current_lunar_phase = calculate_lunar_phase(jdn)

print(current_lunar_phase)

"""
0, 8: New Moon
1: Waning crescent
2: First Quarter
3: Waxing Gibbous
4: Full moon
5: Waning Gibbous
6: Third quarter
7: Waning crescent

"""