from flask import Blueprint, request, redirect, render_template, session
import bcrypt
from models.user import insert_user, get_all_users, get_all_user_cheerups
from helpers.avatar import generate_avatar
from helpers.sessions import get_session_avatar, get_session_user_id
from helpers.jokes import get_rand_joke


user_controller = Blueprint("user_controller", __name__, template_folder="../templates/user")

@user_controller.route('/signup')
def signup():
    return render_template('signup.html')

@user_controller.route('/all-cheerupers')
def show_cheerupers():
    avatar = get_session_avatar()
    user_id = get_session_user_id()
    cheerupers = get_all_users()
    return render_template('all-cheerupers.html', cheerupers=cheerupers, user_id=user_id, avatar=avatar)

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

@user_controller.route('/user-profile/<id>')
def user_profile(id):
    #get currently logged in user
    current_user = get_session_user_id()
    #if the user is not trying to access their own profile, query the database for the users cheerups
    cheerups = get_all_user_cheerups(id)
    avatar = get_session_avatar()

    #check if a user is signed in
    if current_user:
        #if the user is signed, check if the currently signed in user matches the user they're trying to view
        if current_user == int(id):
            #if the signed in user is trying to access their own profile, redirect to /my-profile route
            easter_egg = get_rand_joke()
            return render_template('profile.html', cheerups = cheerups, user_id = current_user, avatar = avatar, current_user = True, easter_egg=easter_egg)

    #check if the user is trying to access a profile that doesn't exist (e.g. manual URL change)
    if len(cheerups) > 0:
        return render_template('profile.html', cheerups = cheerups, user_id = current_user, avatar = avatar, current_user = False)
    else:
        return redirect('/')