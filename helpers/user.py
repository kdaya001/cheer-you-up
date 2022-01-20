import bcrypt
from models.user import get_user_by_email

def check_password(original, entered_password):
    if bcrypt.checkpw(entered_password.encode(), original.encode()):
        return True
    else: 
        return False

def validate_email_exists(email):
    if get_user_by_email(email):
        return False
    else:
        return True