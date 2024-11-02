class PasswordManager:

    def __init__(self, password):
        self.__password = self.__encrypt(password)
    
    def __encrypt(self, password):
        return "32r70343u8e0n03r9g8j7234un_"

    def __decrypt(self):
        
        return "original pass"
    def show_pass(self):
        return self.__decrypt()


p1 = PasswordManager("silv")

print(p1.show_pass())