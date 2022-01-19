import bcrypt

def check_password(original, entered_password):
    if bcrypt.checkpw(entered_password.encode(), original.encode()):
        return True
    else: 
        print('we are not the same')
        return False