from flask import Blueprint, request, redirect, render_template, session, url_for
import bcrypt
from models.user import insert_user, get_all_users, get_all_user_cheerups, get_user_by_id, update_first_name, update_last_name, update_email, update_password, get_all_user_public_cheerups
from helpers.avatar import generate_avatar
from helpers.sessions import get_session_avatar, get_session_user_id
from helpers.jokes import get_rand_joke
from helpers.user import check_password, validate_email_exists


user_controller = Blueprint("user_controller", __name__, template_folder="../templates/user")

#Sign up route
@user_controller.route('/signup')
def signup():
    status_message = request.args.get('status_message')
    status = request.args.get('status')
    return render_template('signup.html', status_message=status_message, status=status)

#Show all users route
@user_controller.route('/all-cheerupers')
def show_cheerupers():
    avatar = get_session_avatar()
    user_id = get_session_user_id()
    cheerupers = get_all_users()
    return render_template('all-cheerupers.html', cheerupers=cheerupers, user_id=user_id, avatar=avatar)

#create user on signup route
@user_controller.route('/create-user', methods=["POST"])
def create_user():
    first_name = request.form.get('f_name')
    last_name = request.form.get('l_name')
    email = request.form.get('email').lower()

    if(validate_email_exists(email)):
        hashed_password = None
        if request.form.get('password_conf_1') == request.form.get('password_conf_2'):
            hashed_password = bcrypt.hashpw(request.form.get('password_conf_1').encode(), bcrypt.gensalt()).decode()

        if hashed_password:
            avatar = generate_avatar()
            session['avatar'] = avatar
            insert_user(first_name, last_name, email, hashed_password, avatar)
            return redirect(url_for('session_controller.login_page', status_message='Successfully created account', status='success'))
        else:
            return redirect(url_for('user_controller.signup', status_message='Failed to make account, try again', status='error'))
    else:
        return redirect(url_for('user_controller.signup', status_message='This email address is already registered', status='error'))

#show user profile route
@user_controller.route('/user-profile/<id>')
def user_profile(id):
    #get currently logged in user
    current_active_user = get_session_user_id()
    #if the user is not trying to access their own profile, query the database for the users cheerups
    cheerups = get_all_user_cheerups(id)
    public_cheerups = get_all_user_public_cheerups(id)
    avatar = get_session_avatar()

    # Get status code if it exists
    status_message = request.args.get('status_message')
    status = request.args.get('status')

    #check if a user is signed in
    if current_active_user:
        #if the user is signed, check if the currently signed in user matches the user they're trying to view
        if current_active_user == int(id):
            #if the signed in user is trying to access their own profile, redirect to /my-profile route
            easter_egg = get_rand_joke()
            return render_template('profile.html', cheerups = cheerups, user_id = current_active_user, avatar = avatar, current_user = True, easter_egg=easter_egg, status=status, status_message=status_message, public_cheerups=public_cheerups)

    #check if the user is trying to access a profile that doesn't exist (e.g. manual URL change)
    if len(cheerups) > 0:
        return render_template('profile.html', cheerups = cheerups, user_id = current_active_user, avatar = avatar, current_user = False, public_cheerups=public_cheerups)
    else:
        return redirect('/')

#update profile details route
@user_controller.route('/update-profile/<id>', methods=["GET","POST"])
def update_profile(id):
    current_user_id = get_session_user_id()
    avatar = get_session_avatar()

    if current_user_id == int(id):
        if request.method == "GET":
            user_details = get_user_by_id(id)
            return render_template('update-profile.html', user_details=user_details[0], user_id = current_user_id, avatar=avatar)
        elif request.method == "POST":
            user_details = get_user_by_id(id)
            first_name = request.form.get('f_name')
        
            if len(first_name) > 0:
                update_first_name(first_name, id)
            last_name = request.form.get('l_name')
        
            if len(last_name) > 0:
                update_last_name(last_name, id)
            email = request.form.get('email')
        
            if len(email) > 0:
                update_email(email, id)

            original_password = user_details[0]['password']
            entered_password = request.form.get('password_conf')
            new_pass_1 = request.form.get('password_conf_1') 
            new_pass_2 = request.form.get('password_conf_2')
        
            if len(entered_password) > 0:
                if check_password(original_password, entered_password):
                    if new_pass_1 == new_pass_2 and len(new_pass_1) > 0:
                        hashed_password = bcrypt.hashpw(new_pass_1.encode(), bcrypt.gensalt()).decode()
                        update_password(hashed_password, id)
                    else:
                        return render_template('update-profile.html', user_details=user_details[0], user_id = current_user_id, avatar=avatar, status_message="Invalid entry. Please try again.", status="error")
                else:
                    return render_template('update-profile.html', user_details=user_details[0], user_id = current_user_id, avatar=avatar, status_message="Invalid entry. Please try again.", status="error")
            elif len(entered_password) == 0 and (len(new_pass_1) > 0 or len(new_pass_2) > 0):
                return render_template('update-profile.html', user_details=user_details[0], user_id = current_user_id, avatar=avatar, status_message="Invalid entry. Please try again.", status="error")

            return redirect(url_for('user_controller.user_profile', id=id,status_message="Successfully updated your profile", status="success"))
    else:
        return redirect('/')