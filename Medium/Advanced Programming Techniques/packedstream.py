original_string  = input("Enter the string:")
packedstring = ""
letter_counter = {}

for i in original_string:
    if not i in letter_counter.keys():
        letter_counter[i] = 1
    else:
        letter_counter[i] += 1

for i, k in letter_counter.items():
    packedstring += (str(i) + str(k))


print(packedstring)