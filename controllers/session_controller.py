import bcrypt
from flask import Blueprint, request, redirect, render_template, session
from models.user import get_user_by_email

session_controller = Blueprint("session_controller", __name__, template_folder="../templates/session")

@session_controller.route('/login')
def loginpage():
    return render_template('login.html')

# login '/sessions/create
@session_controller.route('/sessions/create', methods=["POST"])
def create_session():
    username = request.form.get('username')
    password = request.form.get('password')
    password_valid = False

    user_details = get_user_by_email(username)
    if user_details:
        user_details = user_details[0]
    #check if the user has input both a username and password
    if username and password and user_details:
        password_valid = bcrypt.checkpw(password.encode(), user_details['password'].encode())
        
    if password_valid and username and password:
        session['user_id'] = user_details['id']
        session['first_name'] = user_details['first_name']
        session['avatar'] = user_details['avatar_url']
        return redirect('/')
    else:
        return redirect('/login')

#logout '/sessions/destroy'
@session_controller.route('/sessions/destroy')
def destroy_session():
    session.pop('user_id')
    session.pop('first_name')
    session.pop('avatar')
    return redirect('/')