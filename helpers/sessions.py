from flask import session

def get_session_user_id():
    return session.get('user_id')

def get_session_avatar():
    return session.get('avatar')