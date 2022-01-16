import bcrypt
from flask import Blueprint, request, redirect, render_template, session
from database import sql_write
from models.cheerup import get_all_cheer_ups, insert_cheerup, get_cheerup, remove_cheerup, upvote_cheerup, update_voters, get_top_ten_cheer_ups, get_ten_most_recent_cheerups
from helpers.weather import get_location, get_weather
from models.user import update_score

cheerup_controller = Blueprint("cheerup_controller", __name__, template_folder="../templates/cheerup")

@cheerup_controller.route('/home')
def cheerup_home():
    logged_in_avatar = session.get('avatar')
    user_id = session.get('user_id')
    top_ten_cheerups = get_top_ten_cheer_ups()
    recent_ten_cheerups = get_ten_most_recent_cheerups()
    return render_template('index.html', top_ten_cheerups=top_ten_cheerups, recent_ten_cheerups=recent_ten_cheerups, avatar = logged_in_avatar, user_id = user_id)

@cheerup_controller.route('/cheerup/create', methods=["POST"])
def create_cheerup():
    cheerup = request.form.get('new_cheerup')
    user_id = session.get('user_id')
    visitor_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    city = get_location(visitor_ip)
    weather = None
    if city != None: 
        weather = get_weather(city)
    insert_cheerup(cheerup, user_id, weather)
    return redirect('/')

@cheerup_controller.route('/delete/<id>', methods=["POST"])
def delete_cheerup(id):
    cheerup_details = get_cheerup(id)
    print(cheerup_details)
    if cheerup_details:
        cheerup_details = cheerup_details[0]
    
        if cheerup_details['user_id'] == session.get('user_id'):
            remove_cheerup(id)
            return redirect(request.referrer)
    else: 
        return redirect('/')

#catch if someone enters the URL manually
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