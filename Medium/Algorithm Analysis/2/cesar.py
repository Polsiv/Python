def caesar_encrypt(text, shift):
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            decrypted_text += char 
    return decrypted_text

msg = "Hello There!" 
shift = 13
decrypted_message = caesar_encrypt(msg, shift)
print(decrypted_message)
