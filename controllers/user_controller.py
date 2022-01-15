from flask import Blueprint, request, redirect, render_template, session
import bcrypt
from models.user import insert_user, get_user
from helpers.avatar import generate_avatar
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
def my_profile():
    user_id = session.get('user_id')
    avatar = session.get('avatar')
    if user_id:
        print(user_id)
        user_details = get_user(user_id)
        cheerups = get_user_cheerups(user_id)
        return render_template('my-profile.html', user = user_details[0], cheerups = cheerups, user_id = user_id, avatar=avatar)
    else:
        return redirect('/signup')

@user_controller.route('/user-profile/<id>')
def user_profile(id):
    current_user = session.get('user_id')
    if current_user:
        if current_user == int(id):
            return redirect('/my-profile')

    cheerups = get_user_cheerups(id)
    avatar = session.get('avatar')
    return render_template('user-profile.html', cheerups = cheerups, user_id = current_user, avatar = avatar)