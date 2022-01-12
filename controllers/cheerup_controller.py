import bcrypt
from flask import Blueprint, request, redirect, render_template, session
from models.cheerup import get_all_cheer_ups

cheerup_controller = Blueprint("cheerup_controller", __name__, template_folder="../templates/cheerup")

@cheerup_controller.route('/home')
def cheerup_home():
    cheerups = get_all_cheer_ups()
    return render_template('index.html', cheerups=cheerups)

@cheerup_controller.route('/test')
def test():
    return 'Hello World'