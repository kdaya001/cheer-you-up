import bcrypt
from models.user import get_user_by_email

#check entered password matches database password
def check_password(original, entered_password):
    if bcrypt.checkpw(entered_password.encode(), original.encode()):
        return True
    else: 
        return False

#check if email exists in the database already
def validate_email_exists(email):
    if get_user_by_email(email):
        return False
    else:
        return True