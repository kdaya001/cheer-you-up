import bcrypt
from flask import Blueprint, request, redirect, render_template, session
from database import sql_write
from models.cheerup import get_all_cheer_ups, insert_cheerup, get_cheerup, remove_cheerup, upvote_cheerup, update_voters

cheerup_controller = Blueprint("cheerup_controller", __name__, template_folder="../templates/cheerup")

@cheerup_controller.route('/home')
def cheerup_home():
    logged_in_avatar = session.get('avatar')
    user_id = session.get('user_id')
    cheerups = get_all_cheer_ups()
    return render_template('index.html', cheerups=cheerups, avatar = logged_in_avatar, user_id = user_id)

@cheerup_controller.route('/cheerup/create', methods=["POST"])
def create_cheerup():
    cheerup = request.form.get('new_cheerup')
    user_id = session.get('user_id')
    insert_cheerup(cheerup, user_id)
    return redirect('/')


@cheerup_controller.route('/delete/<id>', methods=["POST"])
def delete_cheerup(id):
    cheerup_details = get_cheerup(id)
    if cheerup_details:
        cheerup_details = cheerup_details[0]
    
    if cheerup_details['user_id'] == session.get('user_id'):
        remove_cheerup(id)
        return redirect('/my-profile')
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
        return redirect('/')