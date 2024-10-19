def rot(string, shift):
    
    d = {i + 1: chr(65 + i) for i in range(26)}
    cipher_msg = ""

    for i in string:  
        letter_pos = list(d.keys())[list(d.values()).index(i)]
        rotated = letter_pos + shift
        
        if rotated > 26:
            cipher_msg += d[rotated - len(d)]
        else:
            cipher_msg += d[rotated]
        
    return cipher_msg
        
message = "hellothere"
shift = 13
print(rot(message.upper(), shift)) 
    