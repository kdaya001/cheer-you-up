import bcrypt
from flask import Blueprint, request, redirect, render_template, session

session_controller = Blueprint("session_controller", __name__, template_folder="../templates/session")

@session_controller.route('/login')
def loginpage():
    return render_template('login.html')

# login '/sessions/create
@session_controller.route('/sessions/create', methods=["POST"])
def create_session():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username,password)

    #check if the user has input both a username and password
    if username and password:
        return redirect('/')
    else:
        return redirect('/login')

#logout '/sessions/destroy'