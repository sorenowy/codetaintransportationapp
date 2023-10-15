import hashlib
from app.config.constants import PASSWORD_SALT

def hash_password(password):
    hashed_password = hashlib.sha512(password.encode('utf-8') + PASSWORD_SALT.encode('utf-8')).hexdigest()
    return hashed_password

def read_hashed_password(user_input_password, hashed_password):
    converted_password = hashlib.sha512(
        user_input_password.encode('utf-8')
        + PASSWORD_SALT.encode('utf-8')
    ).hexdigest()
    
    if converted_password == hashed_password:
        return True
    else:
        return False