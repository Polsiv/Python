import re

def validate_email(email):
    #here: A-Za-z0-9._+- alphanumeric characters that include ._+-
    # []+ means they could be repeated
    pattern = r"\b[A-Za-z0-9._+-]+@[A-Za-z0-9]+\.[A-Za-z]{2,}\b "
    return True if re.findall(pattern, email) else False
        
    
print(validate_email("soporte@hack4u.io"))