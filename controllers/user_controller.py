from flask import Blueprint, request, redirect, render_template, session
import bcrypt
from models.user import insert_user, get_user
from controllers.avatar_controller import generate_avatar
from models.cheerup import get_user_cheerups


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
        avatar = generate_avatar()
        session['avatar'] = avatar
        insert_user(first_name, last_name, email, hashed_password, avatar)
        return redirect('/login')
    else:
        return redirect('/signup')

@user_controller.route('/my-profile')
def user_profile():
    user_id = session.get('user_id')
    if user_id:
        user_details = get_user(user_id)
        cheerups = get_user_cheerups(user_id)
        return render_template('my-profile.html', user = user_details[0], cheerups = cheerups)
    else:
        return redirect('/')