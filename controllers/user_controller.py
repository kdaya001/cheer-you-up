from flask import Blueprint, request, redirect, render_template, session
import bcrypt

user_controller = Blueprint("user_controller", __name__, template_folder="../templates/user")

@user_controller.route('/signup')
def signup():
    return render_template('signup.html')

@user_controller.route('/create-user', methods=["POST"])
def create_user():
    first_name = request.form.get('f_name')
    last_name = request.form.get('l_name')
    email = request.form.get('email')
    
    hashed_password = None
    if request.form.get('password_conf_1') == request.form.get('password_conf_2'):
        hashed_password = bcrypt.hashpw(request.form.get('password_conf_1').encode(), bcrypt.gensalt()).decode()

    if hashed_password:
        return redirect('/login')
    else:
        return redirect('/signup')
        
