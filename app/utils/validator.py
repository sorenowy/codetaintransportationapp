import re  

def validate_email(email) -> bool:  
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
        return True  
    return False  

def validate_password_policy(password) -> bool:
    specialCharacters = [ '$', '@', "!", "#", '%', '^', '&', '*', '(', ')', '_', '-', '?', '.', ',', '[', ']' ]
    result = True
    if len(password) < 8:
        print("Password should be at least 8 character long")
        result = False
        return result
    if not any(char.isdigit() for char in password):
        print("Password should have at least one numeral")
        result = False
        return result
    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        result = False
        return result
    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        result = False
        return result
    if not any(char in specialCharacters for char in password):
        print('Password should have at least one of the symbols $@#')
        result = False
        return result
    if result:
        return result
    