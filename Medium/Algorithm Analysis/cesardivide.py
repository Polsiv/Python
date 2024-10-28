def caesar_decrypt(char, shift):

    if char.isalpha():
        shift_base = 65 if char.isupper() else 97
        decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
        return decrypted_char
    return char

def divide_and_conquer_decrypt(message, shift):

    if len(message) <= 1:
        return caesar_decrypt(message, shift)
    
    mid = len(message) // 2
    left_half = message[:mid]
    right_half = message[mid:]
    
    decrypted_left = divide_and_conquer_decrypt(left_half, shift)
    decrypted_right = divide_and_conquer_decrypt(right_half, shift)
    
    return decrypted_left + decrypted_right

encrypted_message = "ifmmp" 
shift_value = 1
decrypted_message = divide_and_conquer_decrypt(encrypted_message, shift_value)
print(decrypted_message)
