from operator import ge
from flask import Blueprint, request, redirect, render_template, session
from models.cheerup import get_all_cheer_ups, insert_cheerup, get_cheerup, upvote_cheerup, update_voters, get_top_ten_cheer_ups, get_ten_most_recent_cheerups, delete_cheerup
from helpers.weather import get_location, get_weather
from models.user import update_score
from helpers.sessions import get_session_user_id, get_session_avatar

cheerup_controller = Blueprint("cheerup_controller", __name__, template_folder="../templates/cheerup")

@cheerup_controller.route('/home')
def cheerup_home():
    avatar = get_session_avatar()
    user_id = get_session_user_id()
    top_ten_cheerups = get_top_ten_cheer_ups()
    recent_ten_cheerups = get_ten_most_recent_cheerups()
    return render_template('index.html', top_ten_cheerups=top_ten_cheerups, recent_ten_cheerups=recent_ten_cheerups, avatar = avatar, user_id = user_id)

@cheerup_controller.route('/all-cheerups')
def all_cheerups():
    all_cheerups = get_all_cheer_ups()
    user_id = get_session_user_id()
    avatar = get_session_avatar()
    print(all_cheerups)
    return render_template('all-cheerups.html', cheerups=all_cheerups, user_id = user_id, avatar=avatar)

@cheerup_controller.route('/cheerup/create', methods=["POST"])
def create_cheerup():
    cheerup = request.form.get('new_cheerup')
    user_id = get_session_user_id()
    visitor_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    city = get_location(visitor_ip)
    weather = None

    # teesting TODO
    city = "Sydney"

    if city != None: 
        weather = get_weather(city)
    insert_cheerup(cheerup, user_id, weather)
    return redirect('/')

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