from flask import Blueprint, request, redirect, render_template, session, url_for
from models.user import get_user_by_email
from helpers.user import check_password
from helpers.sessions import get_session_avatar, get_session_user_id, get_session_first_name

session_controller = Blueprint("session_controller", __name__, template_folder="../templates/session")

#login screen route
@session_controller.route('/login')
def login_page():
    status_message = request.args.get('status_message')
    status = request.args.get('status')
    return render_template('login.html', status_message = status_message, status = status)

#login session creation route
@session_controller.route('/sessions/create', methods=["POST"])
def create_session():
    username = request.form.get('username').lower()
    password = request.form.get('password')
    password_valid = False

    user_details = get_user_by_email(username)
    if user_details:
        user_details = user_details[0]
    #check if the user has input both a username and password
    if username and password and user_details:
        password_valid = check_password(user_details['password'], password)
        
    if password_valid and username and password:
        session['user_id'] = user_details['id']
        session['first_name'] = user_details['first_name']
        session['avatar'] = user_details['avatar_url']
        return redirect(url_for('cheerup_controller.cheerup_home', status_message="Successfully logged in", status="success"))
    else:
        return redirect(url_for('session_controller.login_page', status_message="Unsuccessful login. Please try again", status="error" ))

#lougout route
@session_controller.route('/sessions/destroy')
def destroy_session():
    if get_session_user_id():
        session.pop('user_id')
    
    if get_session_first_name():
        session.pop('first_name')
    
    if get_session_avatar():
        session.pop('avatar')

    # return redirect('/')
    return redirect(url_for('cheerup_controller.cheerup_home', status_message="Successfully logged out", status="success"))