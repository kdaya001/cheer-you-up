from flask import Blueprint, request, redirect, render_template, session, url_for
from models.cheerup import get_all_public_cheer_ups, insert_cheerup, get_cheerup, upvote_cheerup, update_voters, get_top_ten_public_cheer_ups, get_ten_most_recent_public_cheerups, delete_cheerup, update_cheerup_to_private, update_cheerup_to_public, update_cheerup
from helpers.weather import get_location, get_weather
from models.user import update_score
from helpers.sessions import get_session_user_id, get_session_avatar

cheerup_controller = Blueprint("cheerup_controller", __name__, template_folder="../templates/cheerup")

@cheerup_controller.route('/home')
def cheerup_home():
    avatar = get_session_avatar()
    user_id = get_session_user_id()

    status_message = request.args.get('status_message')
    status = request.args.get('status')

    top_ten_cheerups = get_top_ten_public_cheer_ups()
    recent_ten_cheerups = get_ten_most_recent_public_cheerups()
    return render_template('index.html', top_ten_cheerups=top_ten_cheerups, recent_ten_cheerups=recent_ten_cheerups, avatar = avatar, user_id = user_id, status=status, status_message=status_message)

@cheerup_controller.route('/all-cheerups')
def all_cheerups():
    all_cheerups = get_all_public_cheer_ups()
    user_id = get_session_user_id()
    avatar = get_session_avatar()
    return render_template('all-cheerups.html', cheerups=all_cheerups, user_id = user_id, avatar=avatar)

@cheerup_controller.route('/cheerup/create', methods=["POST"])
def create_cheerup():
    cheerup = request.form.get('new_cheerup')

    user_id = get_session_user_id()
    visitor_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    city = get_location(visitor_ip)
    weather_icon = None

    if city != None: 
        weather_icon = get_weather(city)

    public_visible = True
    if request.form.get('visibility') == 'on':
        public_visible = False
    insert_cheerup(cheerup, user_id, weather_icon, city, public_visible)
    return redirect(url_for('cheerup_controller.cheerup_home', status="success", status_message="Successfully created cheerup"))

@cheerup_controller.route('/delete/<id>', methods=["POST"])
def remove_cheerup(id):
    cheerup_details = get_cheerup(id)
    if cheerup_details:
        cheerup_detail = cheerup_details[0]
        if cheerup_detail['user_id'] == get_session_user_id():
            delete_cheerup(id)
            url = f'/user-profile/{cheerup_detail["user_id"]}'
            return redirect(url)
    else: 
        return redirect(request.referrer)

@cheerup_controller.route('/delete/<id>')
def catch_delete_error(id):
    return redirect('/')

@cheerup_controller.route('/upvote/<id>', methods=["POST", "GET"])
def upvote(id):
    if request.method == "GET":
        return redirect('/')
    elif request.method == "POST":
        upvote_cheerup(id)
        update_voters(session.get('user_id'), id)
        update_score(get_cheerup(id)[0]['user_id'])
        return redirect(request.referrer)

@cheerup_controller.route('/update-visibility/<id>', methods=["POST"])
def update_visibility(id):
    cheerup = get_cheerup(id)
    current_user = get_session_user_id()

    if cheerup:
        current_visibility_status = cheerup[0]['public_visible']
        if current_visibility_status:
            update_cheerup_to_private(id)
            return redirect(url_for('user_controller.user_profile', id=current_user, status="success", status_message="Successfully updated post to Private"))
        else:
            update_cheerup_to_public(id)
            return redirect(url_for('user_controller.user_profile', id=current_user, status="success", status_message="Successfully updated post to Public"))
    else:
        return redirect('/')

@cheerup_controller.route('/edit-cheerup/<id>', methods=["POST"])
def edit_cheerup(id):
    cheerup_edit = request.form.get(f'edited-cheerup-{id}')
    update_cheerup(id, cheerup_edit)
    current_user = get_session_user_id()

    return redirect(url_for('user_controller.user_profile', id=current_user, status="success", status_message="Successfully edited cheerup"))