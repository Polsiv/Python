"""
Author: Juan Pablo Silvestre
"""
import re

class InputManager:

    def read_file(self, file_name):
        """
        reads the file content and removes the left over elements
        """
        num_list = []
        f = open(file_name, "r", encoding='utf-8')
        for i in f:  
            num_list.append(i.strip())
        f.close()
        num_list.remove("100")
        return num_list


class PassWordValidator:

    def check_password(self, passwords):
        """
        checks the passwords and returns the message depending on the password
        """
        verified_passwords = []
        for password in passwords:
            length = " length" * bool(not (
                len(password) >= 8 and len(password) <= 16))
            upper_case = " upper_case" * bool(not re.search(r"[A-Z]", password))
            lower_case = " lower_case" * bool(not re.search(r"[a-z]", password))
            number = " number" * bool(not re.search(r"\d", password))
            special_symbol = " special_symbol" * bool(
                not re.search(r"[!-/]", password))
            invalid = " invalid" * bool(re.search(r"[^A-Za-z0-9!-/]", password))
            passes = ""
            if not (length or upper_case or lower_case or
                    number or special_symbol or invalid):
                passes = "true"
            else:
                passes = "false"
            verified_passwords.append(passes + length + upper_case 
            + lower_case + number + special_symbol + invalid)
        return verified_passwords


class ResultPrinter:

    def show_results(self, passwords, verifiedpasswords):
        """
        displays the results
        """
        for i, k in zip(passwords, verifiedpasswords):
            print(i, k)

class System:

    def __init__(self):
        """
        constructor for System.
        """
        self.fileName = "input.txt"
        self.reader = InputManager()
        self.passwords = self.reader.read_file(self.fileName)
        self.validator = PassWordValidator()
        self.verifed = self.validator.check_password(self.passwords)
        self.resultPrinted = ResultPrinter()

    def show(self):
        """
        calls ResultPrinter instance
        """
        self.resultPrinted.show_results(self.passwords, self.verifed)
      
class Main:
    system = System()
    system.show()
