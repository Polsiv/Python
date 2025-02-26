def romanToInt(s: str):

    inversed_s = ""

    letters = {
        "I" : 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }

    counter, lastvalue = 0, 0
 
    for i in s:
        inversed_s = i + inversed_s

    for i in inversed_s:
        value = letters[i]
        if value < lastvalue: 
            counter -= value
        else:
            counter += value
        lastvalue = value
    print(counter)

    

romanToInt("MCMXCIV")